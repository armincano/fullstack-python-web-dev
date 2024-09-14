-- Active: 1725460995925@@127.0.0.1@5432@pokemon_db
BEGIN;
COPY "pokemones" ("pokedex","nombre","tipo1","tipo2")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/pokemon-db/csv/pokemones-kanto.csv' DELIMITER ','
CSV HEADER;
COPY "capturas" ("pokedex","fecha_captura","lugar","huevo","peso","estatura")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/pokemon-db/csv/capturas.csv' DELIMITER ','
CSV HEADER;
END;