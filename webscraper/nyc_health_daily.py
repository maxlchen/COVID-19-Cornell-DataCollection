"""
Scrape data from NYC Health daily reports
"""
import argparse
import datetime as dt
import logging
import os
import re

import numpy as np
import pandas as pd
import requests
import tabula
from tqdm import tqdm

MAX_VERSION = 2
MAX_AGE = 110
UNKNOWN = "Unknown"
ROW_TEMPLATE = {
    "date": None,
    "country_id": "US",
    "region_id": "NY",
    "subregion": None,
    "sex": None,
    "age_min": None,
    "age_max": None,
    "underlying_conditions": None,
}


def _parse_group(header, group):
    """
    Parse group being split

    Parameters
    ----------
    header: str
        Title of group type (bold text in leftmost column)
    group: str
        Title of group (non-bold text in leftmost column)

    Returns
    -------
    dict[str, any]
        Group specifiers
    """
    # remove superscript numbers
    header = "".join(re.findall(r"[a-zA-Z50 ]", header))
    group = group.replace("-", "").strip()
    if group in "Total" or group == "Number of Confirmed Cases" or group == "Deaths":
        return {}

    # stratified by age
    if header in "Age Group":
        ages = list(map(int, re.findall(r"\d+", group)))
        if re.match(r"\d+ to \d+", group):
            age_min, age_max = ages
            return {"age_min": age_min, "age_max": age_max}
        if re.match(r"\d+ and over", group):
            age_min = ages[0]
            return {"age_min": age_min, "age_max": MAX_AGE}
        if group == "Unknown":
            return {"age_min": UNKNOWN, "age_max": UNKNOWN}
    if header in "Age 50 and over":
        if group == "Yes":
            return {"age_min": 50, "age_max": MAX_AGE}
        if group == "No":
            return {"age_min": 0, "age_max": 50}

    # stratified by gender
    if header in "Sex":
        return {"sex": group}

    # stratified by borough
    if header in "Borough":
        return {"subregion": group}

    # stratified by underlying illness
    if header in "Underlying Illness":
        mapping = {"Yes": True, "No": False, "Pending Investigation": UNKNOWN}
        return {"underlying_conditions": mapping[group]}

    return {}


def _format_summary_table(table, date):
    """
    Format summary table
    """
    # rename columns
    columns = {0: "group", 1: "confirmed_tot"}
    table.rename(columns=columns, inplace=True)

    # parse entries
    formatted = []
    header = ""
    for _, row in table.iterrows():
        if not isinstance(row.confirmed_tot, str) and np.isnan(row.confirmed_tot):
            header = row.group
            continue
        entry = dict(ROW_TEMPLATE)
        entry["date"] = date
        key = "deaths_tot" if row.group == "Deaths" else "confirmed_tot"
        entry[key] = int(row.confirmed_tot.split(" ")[0])
        entry.update(_parse_group(header, row.group))
        formatted.append(entry)

    return formatted


def _format_hospitalization_table(table, date):
    """
    Format hospitalization table
    """
    # rename columns
    columns = {0: "group", 1: "hospitalized_tot", 2: "confirmed_tot"}
    table.rename(columns=columns, inplace=True)

    # parse entries
    formatted = []
    header = ""
    for _, row in table.iterrows():
        if np.isnan(row.confirmed_tot):
            header = row.group
            continue
        entry = dict(ROW_TEMPLATE)
        entry["date"] = date
        entry["hospitalized_tot"] = int(row.hospitalized_tot.split(" ")[0])
        entry["confirmed_tot"] = int(row.confirmed_tot)
        entry.update(_parse_group(header, row.group))
        formatted.append(entry)

    return formatted


def _format_deaths_table_v2(table, date):
    """
    Format deaths table (post Mar-27)
    """
    # rename columns
    columns = {
        0: "group",
        1: True,
        2: False,
        3: UNKNOWN,
        4: None,
    }
    table.rename(columns=columns, inplace=True)

    # parse entries
    formatted = []
    header = ""
    for _, row in table.iterrows():
        if np.isnan(row[None]):
            header = row.group
            continue
        entry = dict(ROW_TEMPLATE)
        for underlying in (True, False, UNKNOWN, None):
            entry = dict(entry)
            entry["date"] = date
            entry["underlying_conditions"] = underlying
            entry["deaths_tot"] = row[underlying]
            entry.update(_parse_group(header, row.group))
            formatted.append(entry)

    return formatted


def _format_deaths_table_v1(table, date):
    """
    Format deaths table (pre Mar-26)
    """
    # rename columns
    columns = {0: "group", 1: "deaths_tot"}
    table.rename(columns=columns, inplace=True)

    # parse entries
    formatted = []
    header = ""
    for _, row in table.iterrows():
        if not isinstance(row.deaths_tot, str) and np.isnan(row.deaths_tot):
            header = row.group
            continue
        entry = dict(ROW_TEMPLATE)
        entry["date"] = date
        entry["deaths_tot"] = int(row.deaths_tot.split(" ")[0])
        entry.update(_parse_group(header, row.group))
        formatted.append(entry)

    return formatted


def _format_deaths_table(table, date):
    """
    Format deaths table
    """
    if len(table.columns) == 2:
        return _format_deaths_table_v1(table, date)
    if len(table.columns) == 5:
        return _format_deaths_table_v2(table, date)
    return []


def _read_table(report, date):
    """
    Read table from NYC Health

    Parameters
    ----------
    report: str
        Type of report: one of ('summary', 'hospitalizations', 'deaths')
    date: dt.date
        Date of data

    Returns
    -------
    list of dict[str, any]
        Formatted table, if found
    """
    base = "https://www1.nyc.gov/assets/doh/downloads/pdf/imm/covid-19-daily-data-summary-{}{}-{}.pdf"

    for version in range(MAX_VERSION, 0, -1):
        name = "" if report == "summary" else "{}-".format(report)
        url = base.format(name, date.strftime("%m%d%Y"), version)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                raise requests.ConnectionError

            # import table from PDF
            tables = tabula.read_pdf(url, pages=1, pandas_options={"header": None})
            table = max(tables, key=lambda t: len(t))

            # remove columns where all entries are nan
            drop = []
            for i, column in enumerate(table.columns):
                try:
                    if np.isnan(table[column]).all():
                        drop.append(column)
                except TypeError:
                    pass
            table.drop(columns=drop, inplace=True)

            # rename columns
            columns = {name: i for i, name in enumerate(table.columns)}
            table.rename(columns=columns, inplace=True)

            # drop rows before "Age Group" & ("Deaths" row)
            errors = {
                "ge Group": "Age Group",
                "umber of Confirmed Cases": "Number of Confirmed Cases",
                "eaths": "Deaths",
            }
            table.replace(errors, inplace=True)
            first = (
                table[0].isin(["Age Group", "Number of Confirmed Cases", "Total"])
            ).idxmax()
            table = table.copy()[first:]
            table = table[table[0] != "Median Age (Range)"]

            table = table.infer_objects()
            return table

        # failure due to timeout (likely data does not exist)
        except requests.ConnectionError:
            logging.info("Timeout for URL: {}".format(url))

    return []


def _read_all_tables(date):
    """
    Read summary/hospitalization/deaths reports
    """
    reports = {
        "summary": _format_summary_table,
        "hospitalizations": _format_hospitalization_table,
        "deaths": _format_deaths_table,
    }
    rows = []
    for report, formatter in reports.items():
        table = _read_table(report, date)
        if len(table):
            rows += formatter(table, date)

    # merge rows with same keys
    parsed = []
    for r2 in rows:
        merged = False
        for r1 in parsed:
            if all(r1[k] == r2[k] for k in ROW_TEMPLATE):
                r1.update(r2)
                merged = True
                break
        if not merged:
            parsed.append(r2)
    return parsed


def _parse_args(args):
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        type=lambda s: dt.datetime.strptime(s, "%Y-%m-%d").date(),
        default=dt.date.today(),
    )
    parser.add_argument("--backfill", action="store_true")
    parser.add_argument("--update", action="store_true")
    return parser.parse_args(args)


def main(args=None):
    """
    Scrape data from NYC health
    """
    # scrape data
    args = _parse_args(args)
    date = args.date
    data = _read_all_tables(date)
    table = True

    # traverse date backwards until no more data found
    if args.backfill:
        pbar = tqdm()
        tqdm.monitor_interval = 0
        while table:
            try:
                pbar.update(1)
                date -= dt.timedelta(1)
                table = _read_all_tables(date)
                data = table + data
            except Exception:
                break

    # append to existing data
    root = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(root, os.pardir, "data")

    if args.update:
        name = max([f for f in os.listdir(data_dir) if f.startswith("nyc")])
        path = os.path.join(data_dir, name)
        current = pd.read_csv(path).to_dict("records")
        data = current + data
        os.remove(path)

    # write to csv
    name = "nyc_daily_health_{}.csv".format(args.date)
    path = os.path.join(data_dir, name)
    pd.DataFrame(data).to_csv(path, index=False)


if __name__ == "__main__":
    main()
