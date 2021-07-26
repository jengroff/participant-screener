# Study Participant Screener

## Overview
### The point of this app is to facilitate the screening of applications from prospective study participants, by 
### bringing the screening flow to SMS and WhatsApp messaging (where many people are more comfortable), 
### and by semi-automating the process. 

## Application Flow
- 

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
