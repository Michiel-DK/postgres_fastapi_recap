# Docker-compose FastAPI + POSTGRES recap

## Get the data

This example dataset consists of multiple .csv files containig airbnb data in multiple cities.

Run below to merge the datasets + filter out a few columns:

```bash
make get_data
```

## Build your images

Build both containers by running below in the terminal:

```bash
docker compose build
```

This will use the **docker-compose.yml** to create the two images:
- *airbnb_api* is a python image containg the code to run the api
- *airbnb_postgres* is a postgres image which will act as the database

## Instantiate your containers

After that you can run below to instantiate two containers from the image:
```bash
docker compose up
```

If you look at the containers in the docker app you will see the directory *postgres_fastapi_recap* which contains:
- *airbnb_api_c* which runs on *http://localhost:8000/*
- *airbnb_postgres_c* which runs on *http://localhost:5432/* (note that here you won't able to do much with the browser)


Note that when you run it for the first time it will run **setup_tables.sql** in the postgres container.

This script does below in order:
1. Creates a database called ***airbnb***
2. Moves into that newly created database
3. Creates an empty table called ***cities*** to populate later
4. Populates the database with our merged.csv
5. Deletes the csv from the image

Also have a look at the **Volumes** tab on the docker-app. You'll see we've created a *postgres_fastapi_recap_pg_data* volume.

This will allow us to persist the database through different instantiations of the containers. Deleting this will delete all your data so watch out!

## Inspect the API

You can then check the api on *http://localhost:8000/* and see how both endpoints are structured.

