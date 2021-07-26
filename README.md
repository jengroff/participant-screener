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
