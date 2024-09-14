-- Active: 1725460995925@@127.0.0.1@5432@umineko_db
BEGIN;
COPY "characters_types" ("character_type_id","type")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/umineko-db/csv/character-types.csv' DELIMITER ','
CSV HEADER;
COPY "characters" ("character_id","first_name","last_name","character_type_id","damage_stat","description")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/umineko-db/csv/characters.csv' DELIMITER ','
CSV HEADER;
END;

BEGIN;
COPY "arcs_categories" ("arc_category_id","name","description")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/umineko-db/csv/arc-categories.csv' DELIMITER ','
CSV HEADER;
COPY "arcs" ("arc_id","arc_category_id","name","description")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/umineko-db/csv/arcs.csv' DELIMITER ','
CSV HEADER;
END;

BEGIN;
COPY "arcs_characters" ("arc_id","character_id")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/umineko-db/csv/arcs-characters.csv' DELIMITER ','
CSV HEADER;
END;