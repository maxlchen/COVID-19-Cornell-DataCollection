# Data Sources

## **Imperial College London Public Health**

https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/covid-19-resources/

+ icl_report8.csv

## **NYC Health**

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

## **Nature Family China Data**
+ Filtered: NatureFamily_China_COVID19_Apr_6_2020.csv
+ Raw: https://github.com/beoutbreakprepared/nCoV2019/blob/master/latest_data/latestdata.csv

| Column                      | Description
| ---                         | ---
| `id`                        | Unique identifier for reported case
| `age`                       | Age of the case reported in year (may be small range or int)
| `sex`                       | Sex
| `city`                      | Initial generic geographic metadata
| `province`                  | Initial entry of name of the first administrative division in which the case is reported
| `country`                   | Name of country in which the case is reported.
| `wuhan(0)_not_wuhan(1)`     | Binary flag to distinguish cases from Wuhan, Hubei, China, from all other cases
| `latitude`                  | Latitude of where the case was reported
| `longitude`                 | Longitude of where the case was reported
| `geo_resolution`            | An indicative field in which the spatial representativeness of “latitude” and “longitude” are described
| `date_onset_symptoms`       | Date when the reported case was recorded to have become symptomatic.  Specific dates are reported as DD.MM.YYYY. Ranges are recorded as DD.MM.YYYY - DD.MM.YYYY
| `date_admission_hospital`   | Date when the reported case was recorded to have been hospitalized. Specific dates are reported as DD.MM.YYYY. Ranges are recorded as DD.MM.YYYY - DD.MM.YYYY.
| `date_confirmation`         | Date when the reported case was confirmed as having COVID-19 using rt-PCR. Confirmation accuracy is contingent on the data source used. Specific dates are reported as DD.MM.YYYY. Ranges are recorded as DD.MM.YYYY - DD.MM.YYYY.
| `symptoms`                  | List of symptoms recorded in the description of the case.
| `lives_in_Wuhan`            | “yes” indicates that the case was a resident of Wuhan.
| `travel_history_dates`      | Recorded travel dates to and from Wuhan. Specific dates are reported as DD.MM.YYYY and indicate date when the individual left Wuhan. Ranges are recorded as DD.MM.YYYY - DD.MM.YYYY when both are available
| `travel_history_location`   | An open field describing the recent recorded travel history of the case.
| `reported_market_exposure`  | “yes” if there was reported market exposure and “no” if there was not
| `additional_information`    | Any additional information that may be informative about the case (occupation, travel, etc)
| `chronic_disease_binary`    | 0 represents a case that was reported to have no chronic disease and 1 represents cases that reported a chronic disease
| `chronic_disease`           | Reported chronic condition(s) of the reported case
| `source`                    | URL identifying source
| `sequence_available`        | accession number for genomic sequence if available
| `outcome`                   | Patients outcome, as either “died” or “discharged” from hospital.
| `date_death_or_discharge`   | Reported date of death or discharge in DD.MM.YYYY format.
| `location`                  | Location of the reported case


## **Italian Health Ministry**

Directory: `data/ita-health` \
Source: https://github.com/pcm-dpc/COVID-19

**Data by Region**
+ dpc-covid19-ita-regioni-YYYYMMDD.csv
    + Have data from Feb. 24, 2020 to Apr. 6, 2020

TODO:
- [ ] Concat all of the CSVs for various dates
- [ ] Gather aggregate data for entire country

| Field Name               | Description                            | Format                       | Example             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        |  Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       |  Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**              | Code of the Region (ISTAT 2019)        | Number                        | 13                  |
| **denominazione_regione**       | Name of the Region                     | Text                         | Abruzzo             |
| **lat**                         | Latitude                               | WGS84                         | 42.6589177          |
| **long**                        | Longitude                              | WGS84                         | 13.70439971         |
| **ricoverati_con_sintomi**      | Hospitalised patients with symptoms    | Number                        | 3                   |
| **terapia_intensiva**           | Intensive Care                         | Number                        | 3                   |
| **totale_ospedalizzati**        | Total hospitalised patients            | Number                        | 3                   |
| **isolamento_domiciliare**      |  Home confinement                       | Number                        | 3                   |
| **totale_positivi** |  Total amount of current positive cases (Hospitalised patients + Home confinement)  | Number                        | 3                   |
| **variazione_totale_positivi**  |  News amount of current positive cases (totale_positivi current day - totale_positivi previous day)  | Number                        | 3                   |
| **nuovi_positivi**  |  News amount of current positive cases (totale_casi current day - totale_casi previous day)  | Number                        | 3                   |
| **dimessi_guariti**             |  Recovered                              | Number                        | 3                   |
| **deceduti**                    | Death                                  | Number                        | 3                   |
| **totale_casi**                 | Total amount of positive cases         | Number                        | 3                   |
| **tamponi**                     | Tests performed                        | Number                        | 3                   |
| **note_it**                     | Notes in italian language (separated by ;)                       | Text                        | pd-IT-000                   |
| **note_en**                     | Notes in english language (separated by ;)                       | Text                        | pd-EN-000                   |
