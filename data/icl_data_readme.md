aggregate_symptom_progression_report8.csv (derived from icl_report8.csv):


| Column                                      | Description                                                                                                                                             |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| grouped_age                                 | the age group that has been aggregated (i.e. 0: 0-9, 10: 10-19, 20: 20-29, etc.)                                                                        |
| country                                     | the country being reported                                                                                                                              |
| reported_cases                              | the number of (published) cases group by Age Group and Country                                                                                          |
| percent_hospitalized                        | the percentage of these patient that have been hospitalized                                                                                             |
| avg_time_to_hospitalisation_if_hospitalised | the mean number of days between hospitalisation and onset of COVID-19, if the patient was hospitalised and the onset date was reported                  |
| percent_death                               | the percentage of these reported cases that ended in death as of the date of this dataset's creation, March 11, 2020                                    |
| percent_recovered                           | the percentage of these reported cases that ended in recovery as of the date of this dataset's creation, March 11, 2020                                 |
| avg_time_to_recovery_if_recovered           | the mean number of days between onset of COVID-19 and recovery, if recovery has been reported                                                           |
| avg_time_to_death_if_death                  | the mean number of days between onset of COVID-19 and death, if death has been reported                                                                 |
| avg_time_symptomatic                        | average difference between number of days between becoming symptomatic and date onset (note: date onset MAY be less than date of becoming aysmptomatic) |


