docker compose build
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
\copy cities FROM 'tmp/merged.csv' DELIMITER ',' CSV HEADER;
