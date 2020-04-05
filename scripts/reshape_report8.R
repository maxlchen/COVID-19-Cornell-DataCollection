library(tidyverse)

#Read Report 8: Data on Symptom Progression
sp = read.csv('../data/icl_report8.csv')
head(sp)

sp$age = as.character(sp$age)
sp = sp[sp$age != 'elderly',]

table(sp$age)
sp$grouped_age = ifelse(sp$age == "<10", "0", sp$age)
table(sp$grouped_age)
sp$grouped_age = as.numeric(gsub("[^0-9.-]", "", sp$grouped_age)) %/% 10 * 10
table(sp$grouped_age)

sp = sp %>%
  mutate(
    date_hospitalised = as.Date(date_hospitalised, format = "%d/%m/%Y"),
    date_onset = as.Date(date_onset, format= "%d/%m/%Y"),
    date_symp_prog1 = as.Date(date_symp_prog1, format= "%d/%m/%Y"),
    date_symp_prog2 = as.Date(date_symp_prog2, format= "%d/%m/%Y"),
    date_symp_prog3 = as.Date(date_symp_prog3, format= "%d/%m/%Y"),
    date_symp_prog4 = as.Date(date_symp_prog4, format= "%d/%m/%Y"),
    date_death = as.Date(date_death, format= "%d/%m/%Y"),
    date_recovered = as.Date(date_recovered, format= "%d/%m/%Y")
  )

# agg_sp : dataframe containing symptom progression aggregated by Age Group and Country, with the following variables:
# grouped_age : the age group that has been aggregated (i.e. 0: 0-9, 10: 10-19, 20: 20-29, etc.)
# country : the country being reported
# reported_cases : the number of (published) cases group by Age Group and Country
# percent_hospitalized : the percentage of these patient that have been hospitalized
# avg_time_to_hospitalisation_if_hospitalised : the mean number of days between hospitalisation and onset of COVID-19, if the patient was hospitalised and the onset date was reported
# percent_death, and percent_recovered : the percentage of these reported cases that ended in death/recovery as of the date of this dataset's creation, March 11, 2020
# avg_time_to_recovery_if_recovered : the mean number of days between onset of COVID-19 and recovery, if recovery has been reported
# avg_time_to_death_if_death : the mean number of days between onset of COVID-19 and death, if death has been reported

agg_sp = sp %>%
  group_by(new_id) %>%
  # mutate(first_date = min(date_onset, date_symp_prog1, date_symp_prog2, date_symp_prog3, date_symp_prog4, na.rm=TRUE)) %>%
  group_by(grouped_age, country) %>%
  summarise(
    reported_cases = n(),
    percent_hospitalized = sum(!is.na(date_hospitalised))/reported_cases,
    percent_death = sum(!is.na(date_death))/reported_cases,
    percent_recovered = sum(!is.na(date_recovered))/reported_cases,
    # avg_time_to_hospitalisation_if_hospitalised = mean(date_hospitalised - first_date, na.rm=TRUE)
    avg_time_to_hospitalisation_if_hospitalised = mean(date_hospitalised - date_onset, na.rm=TRUE),
    avg_time_to_recovery_if_recovered = mean(date_recovered - date_onset, na.rm = TRUE),
    avg_time_to_death_if_death = mean(date_death - date_onset, na.rm=TRUE)
  )

assertthat::assert_that(nrow(sp) == sum(agg_sp$reported_cases))

write.csv(agg_sp, 'aggregate_symptom_progression_report8.csv')
