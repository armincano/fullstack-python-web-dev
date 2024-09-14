-- Active: 1725460995925@@127.0.0.1@5432@pokemon_db
CREATE DATABASE pokemon_db

BEGIN;
CREATE TABLE IF NOT EXISTS pokemones (
    "pokedex" INT,
    "nombre" TEXT,
    "tipo1" TEXT,
    "tipo2" TEXT,
    PRIMARY KEY (pokedex)
);

CREATE TABLE IF NOT EXISTS capturas (
    "captura_id" SERIAL,
    "pokedex" INT,
    "fecha_captura" DATE,
    "lugar" TEXT,
    "huevo" BOOLEAN,
    "peso" DOUBLE PRECISION,
    "estatura" DOUBLE PRECISION,
    PRIMARY KEY (captura_id)
);

ALTER TABLE IF EXISTS capturas
    ADD CONSTRAINT fk_capturas_pokemones_pokedex FOREIGN KEY (pokedex)
    REFERENCES pokemones (pokedex) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
END;