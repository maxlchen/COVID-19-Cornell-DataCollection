# Data Sources

**Imperial College London Public Health**

https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/covid-19-resources/

+ icl_report8.csv

**NYC Health**

https://www1.nyc.gov/site/doh/covid/covid-19-data-archive.page

| Column                      | Description
| ---                         | ---
| `date `                     | Date of report, formatted `YYYY-MM-DD`
| `country_id`                | 2-letter country abbreviation
| `region_id`                 | 2-letter state abbreviation
| `subregion`                 | Name of subregion
| `sex`                       | Sex
| `age_min`                   | Minimum age (inclusive)
| `age_max`                   | Maximum age (inclusive)
| `underlying_conditions`     | Underlying conditions
| `confirmed_tot`             | Cases tested positive (cumulative)
| `hospitalized_tot`          | Cases hospitalized (cumulative)
| `deaths_tot`                | Deaths (cumulative)

Note that an empty cell for a column indicates that an attribute was not split on, which differs from an attribute that is explicitly unknown.

**European CDC Data**

https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

| Column                      | Description
| ---                         | ---
| `dateRep `                  | Date of report, formatted `D/M/YY` and `DD/MM/YYYY`
| `day`                       | Day from dateRep
| `month`                     | Month from dateRep
| `year`                      | Year from dateRep
| `cases`                     | Number of confirmed/reported cases
| `deaths`                    | Number of confirmed/reported deaths
| `countriesAndTerritories`   | Country/Territory being reported
| `geoId`                     | Geographic Region's ID
| `countryterritoryCode`      | Country's Territory Code
| `popData2018`               | Population as of 2018
