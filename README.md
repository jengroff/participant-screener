# Participant Screener

## Overview
This app facilitates the screening of prospective study participants (i.e. applicants), by bringing the screening process to a modality that is more fluid and comfortable for them (SMS and WhatsApp) and through automation, using 
Twilio Studio and Python. 

## Application Flow
- Prospect contacts us through SMS or WhatsApp
- During a full automated session, they:
    - Answer up to 5 screening questions
    - Give us their name and email address
- We store this data, along with their phone number, in a Postgres database
- Non-technical staff can track status and interact with prospects through an admin UI

## Moving parts
- Python, YAML, shell scripts
- Flask, SQLAlchemy, PostgreSQL
- Docker, GitLab CI/CD, Heroku
- Ability to manage the Flask app and the database through the CLI
- Pytest fixtures and tests
- Black code formatting


# Run the app ->

## Docker (recommended):
#### Use docker-compose to build the image and run the container:
```
docker-compose up -d --build
```

## Create the database schema:
```
docker-compose exec api python manage.py recreate_db'
```
    
## Seed the database:
```
docker-compose exec api python manage.py seed_db'
```
