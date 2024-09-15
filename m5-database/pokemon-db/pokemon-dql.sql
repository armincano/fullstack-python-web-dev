-- Active: 1725460995925@@127.0.0.1@5432@pokemon_db
-- Mostrar todas las columnas de la tabla y las filas con sus registros
SELECT * FROM pokemon;

-- mostrar columna(s) en específico con sus filas
SELECT "location", pokedex FROM captures;

--WHERE clause: mostrar filas que contienen un valor condicionado en una columna especifica
SELECT * FROM captures
WHERE "location" = 'Santiago';

-- mostrar filas cuando se cumpla una de las condiciones
SELECT "name", type1, type2 FROM pokemon
WHERE type1 = 'poison' OR type2 = 'poison';

SELECT * FROM captures
WHERE "weight" BETWEEN 50 AND 100
ORDER BY "weight";

-- mostrar cuando NO se cumplan ambas condiciones
-- BE CAREFUL WITH NULL VALUES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
--there are 8 fighting type pokemon, 1 of them is defined along type2 column, the other 7 are defined along type1 column
SELECT * FROM pokemon
WHERE type1 = 'fighting' OR type2 = 'fighting';
-- I think that if retrieve all types different to 'fighting' type (143 pokemon),
--it will show all pokemon that have a type1 different to 'fighting' and type2 different to 'fighting'
-- but only retrieve 61 pokemon
SELECT * FROM pokemon
WHERE type1 != 'fighting' AND type2 != 'fighting';
--My logic is wrong, I was missing a condition: the NULL values.
--Comparisons with `NULL` using `!=` or `=` will always result in `NULL` (unknown), not `TRUE` or `FALSE`
--To compare a column with `NULL`, you must use the `IS NULL` or `IS NOT NULL` operators
SELECT * FROM pokemon
WHERE type1 != 'fighting' AND type2 != 'fighting'
OR type1 != 'fighting' AND type2 IS NULL;


-- mostrar cuando se cumplan ambas condiciones
SELECT * FROM pokemon
WHERE type1 = 'water' AND type2 = 'ice' OR type1 = 'ice' AND type2 = 'water'
ORDER BY 1 DESC;

-- count occurrences for each distinct value in a column
-- notice that type2 is NOT CONSIDERED
--14 rows. 'flying' type is only present in type2 column
SELECT type1, Count(*) AS pkm_count
FROM pokemon
GROUP BY type1
ORDER BY 2 DESC;
-- SOLUTION to consider type2 ang get all different pkm types:
--UNION ALL To get the values of both columns (type1 and type2) as if they were a single column
--15 rows
SELECT "type", COUNT(*) AS pkm_count
FROM (
    SELECT type1 AS "type"
    FROM pokemon
    UNION ALL
    SELECT type2 AS "type"
    FROM pokemon
    WHERE type2 IS NOT NULL
) AS combined_types
GROUP BY "type"
ORDER BY pkm_count DESC;

-- Indicar la cantidad de pokemon capturados por comuna
SELECT "location", Count(*) AS captured_pkm_count
FROM captures
GROUP BY "location";

/* FUNCIONES */
-- LENGTH() -mostrar la cantidad de caracteres de una columna
SELECT "name", LENGTH("name") AS name_length
FROM pokemon
LIMIT 10;

/* IN() NOT IN() */
SELECT * FROM pokemon -- IN multiples valores posibles en una columna
WHERE type1 IN ('fighting') OR type2 IN ('fighting')
ORDER BY 3 DESC;

SELECT * FROM pokemon -- NOT IN
WHERE type1 NOT IN ('fighting') AND type2 NOT IN ('fighting')
OR type1 NOT IN ('fighting') AND type2 IS NULL
ORDER BY 3 DESC;

-- Concatenar columnas
SELECT type1, STRING_AGG("name", ', ') AS pkm_names
FROM pokemon
GROUP BY type1;

-- DISTINCT clause
--mostrar valores distintos para las combinaciones de dos columnas
SELECT DISTINCT type1, type2
FROM pokemon
ORDER BY 1 ASC;

-- COUNT()
SELECT pokedex, COUNT(*) AS "distinct_captured_pkm"
FROM captures
GROUP BY pokedex;

-- MAX() MIN()
SELECT
	CONCAT(MAX("height"),' ','mts.') AS "tallest_pkm",
    CONCAT(MIN("weight"),' ','kgs.') AS "lightest_pkm"
FROM captures;

-- ROUND() AVG()
SELECT ROUND(AVG("weight")) || ' kgs.' AS "average_pkm_weight"
FROM captures;

-- inner join
SELECT 
	po.pokedex,
	po.name,
    po.type1,
    po.type2,
    ca.location,
    ca.capt_date
FROM pokemon po
JOIN captures ca ON po.pokedex = ca.pokedex;

-- find Pokemon that have not been captured
-- Returns all records from the left table, along the matching records from the right table.
-- the WHERE clause will filter the records that have a NULL value in the right table
SELECT
	po.pokedex,
	po.name,
    ca.capt_date
FROM pokemon po
LEFT JOIN captures ca ON po.pokedex = ca.pokedex
WHERE ca.capt_date IS NULL;

-- count the number of Pokemon captured by location
SELECT 
	ca.location,
    COUNT(ca.location) AS "qty_captured_pkm"
FROM captures ca
INNER JOIN pokemon po ON ca.pokedex = po.pokedex
GROUP BY ca.location
ORDER BY 2 DESC;

--EXTRA MATERIAL: https://thelawrenceq.medium.com/top-sql-queries-you-should-know-using-the-pok%C3%A9mon-dataset-ba76840dbc37