"""
Scrape data from Louisiana health
"""
import datetime as dt
import os
import re
from io import BytesIO

import pytesseract
import requests
from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image, ImageFile
from tqdm import tqdm

# ventilator data only back to 3/25
MIN_DATE = dt.datetime.strptime("2020-03-26", "%Y-%m-%d")
ImageFile.LOAD_TRUNCATED_IMAGES = True


def _get_image_links():
    """
    Get all links to screenshots
    """
    url = "https://covidtracking.com/data/state/louisiana"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.findAll("li")
    images = []
    for link in links:
        dest = link.find("a").get("href")
        if dest.endswith("png"):
            images.append(dest)
    return images


def _parse_timestamp(link):
    """
    Parse timestamp from URL
    """
    # parse date of screenshot
    date, time = re.findall(r"\d+", link)
    timestamp = dt.datetime.strptime(date + time, "%Y%m%d%H%M%S")
    return timestamp


def _get_patient_data(link):
    """
    Get number of hospitalizations & patients on ventilators
    """
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    # only use text in top right
    boxes = list(zip(*[data[k] for k in ("left", "top", "width", "height")]))
    width, height = img.size
    indices = []
    for i, (l, t, w, h) in enumerate(boxes):
        if l / width > 0.70 and t / height < 0.15:
            indices.append(i)
    text = " ".join([data["text"][i] for i in indices])

    # number of hospitalizations
    try:
        pattern_h = r"COVID-19 Patients in Hospitals \d+(?:,\d+)?"
        hospitalized = re.findall(pattern_h, text)[0]
        num_hospitalized = int(hospitalized.split(" ")[-1].replace(",", ""))
    except IndexError:
        num_hospitalized = None

    # number of patients on ventilators
    try:
        pattern_v = r"\d+(?:,\d+)? of those on ventilators"
        ventilators = re.findall(pattern_v, text)[0]
        num_ventilators = int(ventilators.split(" ")[0].replace(",", ""))
    except IndexError:
        num_ventilators = None

    return {
        "timestamp": str(_parse_timestamp(link)),
        "num_hospitalized": num_hospitalized,
        "num_ventilators": num_ventilators,
    }


def main():
    """
    Scrape all data
    """
    # read current file
    root = os.path.dirname(os.path.abspath(__file__))
    name = "louisiana_health.csv"
    path = os.path.join(root, os.pardir, "data", name)
    current = pd.read_csv(path).to_dict("records")

    links = _get_image_links()
    data = []
    for link in tqdm(links):
        timestamp = _parse_timestamp(link)
        if timestamp <= MIN_DATE:
            break
        if str(timestamp) not in [r["timestamp"] for r in current]:
            result = _get_patient_data(link)
            current.append(result)

    # re-write to csv
    update = pd.DataFrame(current).sort_values("timestamp")
    update.to_csv(path, index=False)


if __name__ == "__main__":
    main()
