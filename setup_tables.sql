CREATE DATABASE airbnb;
\c airbnb
CREATE TABLE cities (
  id INT PRIMARY KEY,
  city TEXT,
  room_price REAL,
  host_is_superhost boolean,
  bedrooms INT,
  satisfaction REAL
);
\copy cities FROM 'merged.csv' DELIMITER ',' CSV HEADER;
\! rm merged.csv