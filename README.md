# Docker-compose FastAPI + POSTGRES recap

## Run the preprocess.ipynb



## Build your containers

Build both containers by running below in the terminal:

```bash
docker compose build
```

This will use the **docker-compose.yml** to create the two containers.

After that you can run below to instantiate two containers from the images.
```bash
docker compose up
```

Note that when you run it for the first time it will run **setup_tables.sql** in the postgres container.

This script does below in order:
1. Creates a database called ***airbnb***
2. Moves into that newly created database
3. Creates an empty table called ***cities*** to populate later
4. Populates the database with our merged.csv
5. Deletes the csv from the image






Then run
docker compose up
docker cp raw_data/merged.csv $POSTGRES_CONTAINER:/tmp
docker exec -it $POSTGRES_CONTAINER psql -U $POSTGRES_USER
CREATE DATABASE airbnb_2;
CREATE TABLE cities (
  id INT PRIMARY KEY,
  city TEXT,
  room_price REAL,
  host_is_superhost boolean,
  bedrooms INT,
  satisfaction REAL
);
\copy cities FROM 'merged.csv' DELIMITER ',' CSV HEADER;
