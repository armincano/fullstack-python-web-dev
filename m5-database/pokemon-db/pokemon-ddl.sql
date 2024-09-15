-- Active: 1725460995925@@127.0.0.1@5432@pokemon_db
CREATE DATABASE pokemon_db;

BEGIN;
CREATE TABLE IF NOT EXISTS pokemon (
    "pokedex" INT,
    "name" TEXT,
    "evolutions_num" INT,
    "types_num" INT,
    "type1" TEXT,
    "type2" TEXT,
    "capt_rate" INT,
    "hp" INT,
    "attack" INT,
    "defense" INT,
    "special" INT,
    "speed" INT,
    "normal_dmg" DOUBLE PRECISION,
    "fire_dmg" DOUBLE PRECISION,
    "water_dmg" DOUBLE PRECISION,
    "electric_dmg" DOUBLE PRECISION,
    "grass_dmg" DOUBLE PRECISION,
    "ice_dmg" DOUBLE PRECISION,
    "fight_dmg" DOUBLE PRECISION,
    "poison_dmg" DOUBLE PRECISION,
    "ground_dmg" DOUBLE PRECISION,
    "flying_dmg" DOUBLE PRECISION,
    "psychic_dmg" DOUBLE PRECISION,
    "bug_dmg" DOUBLE PRECISION,
    "rock_dmg" DOUBLE PRECISION,
    "ghost_dmg" DOUBLE PRECISION,
    "dragon_dmg" DOUBLE PRECISION,
    "is_legendary" BOOLEAN,
    PRIMARY KEY (pokedex)
);

CREATE TABLE IF NOT EXISTS captures (
    "capture_id" SERIAL,
    "pokedex" INT,
    "capt_date" TIMESTAMP WITHOUT TIME ZONE,
    "location" TEXT,
    "was_egg" BOOLEAN,
    "weight" REAL,
    "height" REAL,
    PRIMARY KEY (capture_id)
);

ALTER TABLE IF EXISTS captures
    ADD CONSTRAINT fk_captures_pokemon_pokedex FOREIGN KEY (pokedex)
    REFERENCES pokemon (pokedex) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
END;