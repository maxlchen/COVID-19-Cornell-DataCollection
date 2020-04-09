wget -O ../data/covid_tracking_states_daily.csv https://covidtracking.com/api/v1/states/daily.csv
git add ../data/covid_tracking_states_daily.csv
git commit -m "Update State daily data"
git push
