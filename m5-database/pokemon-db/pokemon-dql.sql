-- Active: 1725460995925@@127.0.0.1@5432@pokemon_db
-- Mostrar todas las columnas de la tabla y las filas con sus registros
SELECT * FROM pokemones;

-- mostrar columna(s) en específico con sus filas
SELECT lugar, pokedex FROM capturas;

--WHERE clause: mostrar filas que contienen un valor condicionado en una columna especifica
SELECT * FROM capturas
WHERE lugar = 'Santiago';

-- mostrar filas cuando se cumpla una de las condiciones
SELECT nombre, tipo1, tipo2 FROM pokemones
WHERE tipo1 = 'veneno' OR tipo2 = 'veneno';

SELECT * FROM capturas
WHERE peso BETWEEN 50 AND 100
ORDER BY peso;

-- mostrar cuando NO se cumplan ambas condiciones
SELECT * FROM pokemones
WHERE tipo1 != 'bicho' AND tipo2 != 'bicho';

-- mostrar cuando se cumplan ambas condiciones
SELECT * FROM pokemones
WHERE tipo1 = 'agua' AND tipo2 = 'hielo' OR tipo1 = 'hielo' AND tipo2 = 'agua'
ORDER BY 1 DESC;

-- contar las coincidencias de cada valor distinto
SELECT tipo1, Count(*) AS total
FROM pokemones
GROUP BY tipo1;

-- Indicar la cantidad de pokemones capturados por comuna
SELECT lugar, Count(*) AS total
FROM capturas
GROUP BY lugar;

/* FUNCIONES */
-- LENGTH() -mostrar la cantidad de caracteres de una columna
SELECT nombre, LENGTH(nombre) AS largo_del_nombre
FROM pokemones
LIMIT 10;

/* IN() NOT IN() */
SELECT * FROM pokemones -- IN multiples valores posibles en una columna
WHERE tipo1 IN ('roca','agua','hielo','bicho')
ORDER BY 3 DESC;

SELECT * FROM pokemones -- NOT IN
WHERE tipo1 NOT IN ('roca','agua','hielo','bicho')
ORDER BY 3 DESC;

-- Concatenar columnas
SELECT tipo1, STRING_AGG(nombre, ', ') AS pokemon_names
FROM pokemones
GROUP BY tipo1;

-- DISTINCT clause -mostrar solo valores distintos en columna
SELECT DISTINCT tipo1
FROM pokemones
ORDER BY 1 ASC;

-- COUNT()
SELECT pokedex, COUNT(*) AS "pokemon_distintos_capturados"
FROM capturas
GROUP BY pokedex;

-- MAX() MIN()
SELECT
	CONCAT(MAX(estatura),' ','mts.') AS "Pokemon más alto mide",
    CONCAT(MIN(peso),' ','kgs.') AS "Pokemon más liviano pesa"
FROM capturas;

-- ROUND() AVG()
SELECT ROUND(AVG(peso)) || ' kgs.' AS "Promedio peso de los pokemon"
FROM capturas;

-- inner join
SELECT 
	po.pokedex,
	po.nombre,
    po.tipo1,
    po.tipo2,
    ca.lugar,
    ca.fecha_captura
FROM pokemones po
JOIN capturas ca ON po.pokedex = ca.pokedex;

-- Indicar pokemon no capturado
-- Returns all records from the left table, and the matching records from the right table.
SELECT
	po.pokedex,
	po.nombre,
    ca.fecha_captura
FROM pokemones po
LEFT JOIN capturas ca ON po.pokedex = ca.pokedex
WHERE ca.fecha_captura IS NULL;

-- Indicar cuantos pokemones se capturaron POR comuna.
SELECT 
	ca.lugar,
    COUNT(ca.lugar) AS "Cantidad"
FROM capturas ca
INNER JOIN pokemones po ON ca.pokedex = po.pokedex
GROUP BY ca.lugar
ORDER BY 2 DESC;