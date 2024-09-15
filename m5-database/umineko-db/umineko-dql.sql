-- Active: 1725460995925@@127.0.0.1@5432@umineko_db
--SELECT statement
SELECT * FROM "characters";

--WHERE clause: Filter data based on specific criteria.
SELECT * FROM "characters"
WHERE "first_name" = 'Battler';

--LIMIT: Limit the number of rows returned by a query.
--ORDER BY clause: Sort data based on specific criteria.
SELECT * FROM "characters"
ORDER BY first_name
LIMIT 5;

--COUNT function: Count the number of rows returned by a query.
SELECT COUNT(*)
FROM "characters"
WHERE last_name = 'Ushiromiya';

--SUM function: Calculate the sum of a column.
SELECT SUM(damage_stat) AS ushiromiya_total_damage
FROM "characters"
WHERE last_name = 'Ushiromiya';

--AVG function: Calculate the average of a column.
SELECT AVG(damage_stat) AS ushiromiya_avg_damage
FROM "characters"
WHERE last_name = 'Ushiromiya';

--GROUP BY clause: Group rows based on specific criteria.
SELECT damage_stat, COUNT(*)
FROM "characters"
GROUP BY damage_stat
ORDER BY damage_stat;

--JOIN clause: Combine data from multiple tables.
SELECT ch.first_name, cht.type FROM "characters" ch
JOIN "characters_types" cht ON ch.character_type_id = cht.character_type_id;

--DISTINCT clause: Retrieve unique values from a column.
SELECT DISTINCT "damage_stat"
FROM "characters"
ORDER BY "damage_stat";

--Subqueries: Use a query inside another query.
--e.g: retrive all the characters that participate in the first arc
SELECT * FROM "characters"
WHERE "character_id" IN (
    SELECT "character_id" FROM "arcs_characters"
    WHERE "arc_id" = 1
);
--Can do it with JOIN
SELECT * FROM "characters" ch
JOIN "arcs_characters" ac ON ch."character_id" = ac."character_id"
WHERE ac."arc_id" = 1;

--UNION operator: Combine the results of two or more SELECT statements.
--e.g: retrieve all the characters that are demons and angels
SELECT * FROM "characters"
WHERE character_type_id = 7
UNION
SELECT * FROM "characters"
WHERE character_type_id = 9
ORDER BY character_type_id;

--EXCEPT operator: Retrieve records from the first query that are not present in the second query.
--e.g.:retrieve all characters from the first arc that are not present in the third arc. Bernkastel is the only one.
SELECT character_id FROM arcs_characters
WHERE arc_id = 1
EXCEPT
SELECT character_id FROM arcs_characters
WHERE arc_id = 3;

--Classify the characters by their damage stat. using low(1-3), medium(4-7), high(8-9), ultra_high(10) categories.
SELECT first_name, damage_stat,
    CASE
        WHEN damage_stat BETWEEN 1 AND 3 THEN 'low'
        WHEN damage_stat BETWEEN 4 AND 7 THEN 'medium'
        WHEN damage_stat BETWEEN 8 AND 9 THEN 'high'
        ELSE 'ultra_high'
    END AS damage_category
FROM "characters"
ORDER BY damage_stat DESC;

--List the characters with the most common damage stat.
SELECT * FROM "characters" ch
WHERE ch.damage_stat = (
    SELECT damage_stat
    FROM "characters"
    GROUP BY damage_stat
    ORDER BY COUNT(*) DESC
    LIMIT 1
);