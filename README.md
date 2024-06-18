<img src="https://lcarvajal.github.io/img/open-data-austria.png" height=100>

# Real Open Data

A React + Django web app that makes data from [Open Data Austria](https://www.data.gv.at/en/) more accessible to less data-savvy people.

### Problem

I tried investigating data sets from [Open Data Austria](https://www.data.gv.at/en/) but found it to be extremely cumbersome.

In an effort to make the process faster, I built an ETL pipeline that pulls all their datasets using their API, cleans it (removing loads of data sets that are not very useful), and store it locally on my computer for analysis.

When I analyzed some of these cleaned up datasets and shared my findings with less data-savvy people, I got all kinds of interesting questions but it would take a while for me to get back to them. So I set out to make it easy for people to answer their questions themselves.

### Developing a Solution

I developed an ETL pipeline (separate project) extracts 800+ datasets from Open Austria, removes useless ones, and cleans up datasets so that they can get displayed through the Web App.

#### ETL Pipeline Technologies
- Pandas

### Web App Technologies
- React
- Django
- Pandas

## Support
- Vienna data on dogs, population, and unemployment.

## Setup
 - Django - python manage.py runserver, python manage.py collectstatic
 - PostgreSQL - brew services start postgresql@16

## To-dos
1. Host app with Docker
