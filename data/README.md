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

**ICNARC COVID-19 Report**

https://www.icnarc.org/About/Latest-News/2020/04/04/Report-On-2249-Patients-Critically-Ill-With-Covid-19

Report done by ICNARC containing data on cases from critical care units in England, Wales, and Northern Ireland, including duration of advanced respiratory support.
Pdf file has more data than what is on table, but the table has the more important values.

| Label                                           | Description
| ---                                             | ---
| `Age mean `                                     | Mean of age of patients 
| `Age median`                                    | Mean of age of patients 
| `Female`                                        | Female
| `Male`                                          | Male
| `No assistance`                                 | Number of Patients that didn't require assistance prior to hospitalization
| `Some assistance`                               | Number of Patients that required some assistance prior to hospitalization
| `Total assistance`                              | Number of Patients that required total assistance prior to hospitalization
| `Ventilator in 24h`                             | Number of patients that received a ventilator in 24 hours
| `Alive`                                         | Number of patients in critical care who were discharged alive
| `Dead`                                          | Number of patients in critical care who died
| `Survivor`                                      | Average # of days patient stayed and was successfully discharged
| `Non-survivor`                                  | Average # of days patient stayed and then died
| `Duration of advanced respiratory support`      | Average # of days patient received advanced respiratory support
| `Duration of total respiratory support`         | Average # of days patient received advanced + basic respiratory support
