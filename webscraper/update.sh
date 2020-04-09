#!/bin/bash
pipenv run python nyc_health_daily.py --update
pipenv run python louisiana_health.py
git add -A
git commit -m "Update NYC & Louisiana data"
git push