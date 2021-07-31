# Automated Applicant Screener

## Overview
Mobile messaging assistant which interacts with, and captures data from, research study applicants. 

## Application Flow
- App responds to inbound SMS or WhatsApp messages from users; 
- During a fully automated session, the app: 
    - Asks an applicant 3 - 8 screening questions, to help determine study fit;
    - Captures all the prospect's responses, as well as their phone number, email address, and name; 
- Stores it all in a PostgreSQL database;
- Presents it all in a Web UI for non-technical staff to view, edit, and track. 

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
