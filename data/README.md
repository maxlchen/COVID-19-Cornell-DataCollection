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
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|
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

## **European CDC Data**

Source: https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

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

## **ICNARC COVID-19 Report**

Source: https://www.icnarc.org/About/Latest-News/2020/04/04/Report-On-2249-Patients-Critically-Ill-With-Covid-19

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

## **Louisiana Department of Health**

Screenshots via https://covidtracking.com/data/state/louisiana

| Column                | Description
| ---                   | ---
| `timestamp`           | Timestamp of screenshot, as deduced from URL
| `num_hospitalized`    | Total number of hospitalized patients
| `num_ventilators`     | Total number of patients on ventilators

## **Governor Cuomo Daily Briefing Data**
Sources: 
* https://www.news10.com/wp-content/uploads/sites/64/2020/04/04.05.20-COVID19-Briefing.pdf
* https://www.youtube.com/channel/UCLHU6ECVSZbzgcpd113Jk4Q


Data scraped from NY Governor Andrew Cuomo's daily briefings.
All data is for the state of New York, unless explictly stated. Data includes change in hospitalizations, change in intubations, daily discharges, and number of deaths. As well as total 
hospitalization percentages in NYC vs. Long Island vs. Downstate vs. Upstate. 
Only data reported in the briefing is populated, not all data is populated. This is manually curated on a relatively active basis

| Column                      | Description
| ---                         | ---
| `date`                  | Date of report, formatted `MM/DD/YY`
| `total_new_hospitalizations`                       | Number of new hospitalizations each day in NYS. "Total New Hospitalizations" as reported in the daily briefing. New hospitalizations each day in the state of New York.
| `change_in_daily_icu_admissions`                     | Number of new ICU admissions each day. "Change in Daily ICU Admissions" as reported in the briefing. Positive number indicates an increase in total admits.
| `change_in_daily_intubations`                     | Number of new intubations each day. "Change in Daily Intubations" as reported in the briefing. 
| `change_in_daily_discharge`                      | Number of new discharges each day. "Change in Daily Discharged" as reported in the briefing.
| `number_of_deaths`                     | Number of deaths each day. "Number of Deaths" as reported in the briefing. 
| `percent_TOTAL_hospitalized_in_nyc`                    | Percentage of total hospitalizations that were in New York City, rounded.
| `percent_TOTAL_hospitalized_in_long_island`   | Percentage of total hospitalizations that were in Long Island, rounded.
| `percent_TOTAL_hospitalized_in_westchester_and_rockland`                     | Percentage of total hospitalizations that were in Westchester and Rockland, rounded.
| `percent_TOTAL_hospitalized_in_rest_NYS`      | Percentage of total hospitalizations that were in the rest of New York State. This includes all hospitalizations in New York State outside of NYC, Long Island, Westchester, and Rockland, rounded. 


## **Japanese Ministry of Health, Labour, & Welfare**

Source: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000121431_00086.html

| Column                | Description
| ---                   | ---
| `date`                | Date of report, formatted `YYYY-MM-DD`
| `patients`            | Total number of current patients: this is the sum of `non_serious`, `ventilator_icu`, `pending_diagnosis`, `waiting`, and `pending_symptoms`
| `non_serious`         | Total number of current patients with light to moderate symptoms
| `ventilator_icu`      | Total number of current patients on ventilator or in ICU
| `pending_diagnosis`   | Total number of current patients with symptoms but pending categorization into two preceding categories
| `waiting`             | Total number of patients waiting to be admitted to hospital
| `pending_symptoms`    | Total number of patients waiting to be determined as symptomatic or asymptomatic
| `recovered`           | Cumulative total of patients who were admitted to hospital and subsequently released
| `deceased`            | Cumulative total of deaths


## **Laboratory-Confirmed COVID-19-Associated Hospitalizations**


https://gis.cdc.gov/grasp/COVIDNet/COVID19_3.html

Click "Download Data", then "Custom Download", click "Surveillance Area", and select an area (i.e. "--New York"). Finally, click Select All Age Groups.

COVID-19Surveillance_EIP_New_York_Data.csv updated March 28, 2020:


| Column                                      | Description                                                                                                                                             |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| CATCHMENT                                   | Surveillance Area (in this case, New York)                                                                        										|
| NETWORK                                     | EIP for all values                                                                                                                             			|
| YEAR                                        | Year being reported (2020 for all)							                                                                                            |
| MMWR-YEAR                                   | Epidemiologic Year (2020 for all)						                                                                                                |
| MMWR-WEEK                                   | Week of the epidemiologic year (1 corresponds to the first week of 2020 with at least 4 days; 10 corresponds to Week Ending March 7, 2020).             |
| AGE CATEGORY                                | Age Group, e.g. 0-4 yr or 65+ year 																									                    |
| CUMULATIVE RATE                             | The Cumulative Rate of Hospitalization of all weeks up until this row's MMWR-WEEK                                    									|
| WEEKLY RATE                            	  | The Rate of Hospitalization of this row's MMWR-WEEK                                																		|

## **Public Health Agency of Canada**

Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310076601

Offers per-patient level data

| Column                | Description
| ---                   | ---
| `case_num`                | Case number for patient
| `last_update_date`            | The date of the last update to the case
| `onset_date`         | The earliest date available from the following series: Symptom Onset Date, Specimen Collection Date, Laboratory Testing Date, PHAC Reported Date
| `sex`      | Gender of patient
| `age_group`   | Age group the patient falls under
| `transmission`             | Method in which the patient contracted COVID-19
| `is_hospitalized`    | Whether patient is hospitalized
| `ICU`           | Whether patient is in the intensive care unit (ICU)
| `is_deceased`            | Whether the patient is deceased
| `prev_is_hospitalized`    | Whether or not patient's hospitalization status has changed, and if so, from what
| `prev_ICU`           | Whether or not patient's ICU status has changed, and if so, from what
| `prev_is_deceased`            | Whether or not patient's life status has changed, and if so, from what

## **CovidTracking**

+ Source: https://covidtracking.com/api/v1/states/daily.csv
+ Raw: `covid_tracking_states_daily.csv`

**TODO**: Table for columns 
