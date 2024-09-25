-- Active: 1725460995925@@127.0.0.1@5432@dvdrental
--1.1 Escribe consultas para insertar un Customer, Staff y Actor.
BEGIN;
INSERT INTO "address" ("address", district, city_id, postal_code, phone) VALUES ('Carrer de lHarmonia, 2', 'Barcelona', 55, '08035', '932123456');
INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool)
VALUES (1, 'Armin','Cano','arminpuertomontt@gmail.com',606,true);
INSERT INTO staff (first_name, last_name, address_id, email, store_id, "active", "username", "password")
VALUES ('Armin','Cano',606,'arminpuertomontt@gmail.com',1,true,'armin','12345');
INSERT INTO actor (first_name, last_name) VALUES ('Ariana', 'Granda');
END;

--1.2 Escribe consultas para modificar un Customer, Staff y Actor.
BEGIN;
UPDATE "address" SET "address" = 'Carrer de l''Harmonia, 2' WHERE "address" = 'Carrer de lHarmonia, 2';
UPDATE customer SET email = 'arminbarcelona@gmail.com' WHERE customer_id = 600;
UPDATE staff SET email = 'arminbarcelona@gmail.com' WHERE staff_id = 3;
UPDATE actor SET last_name = 'Grande' WHERE actor_id = 201;
END;

--1.3 Escribe consultas para eliminar un Customer, Staff y Actor.
BEGIN;
DELETE FROM customer WHERE customer_id = 600;
DELETE FROM staff WHERE staff_id = 3;
DELETE FROM actor WHERE actor_id = 201;
END;

SELECT * FROM "address" WHERE address = 'Carrer de lHarmonia, 2';
SELECT * FROM "address" WHERE address = 'Carrer de l''Harmonia, 2';
SELECT * FROM customer WHERE first_name = 'Armin';
SELECT * FROM staff WHERE first_name = 'Armin';
SELECT * FROM actor WHERE first_name = 'Ariana';

--2 Listar todas las “rental” con los datos del “customer” dado un año y mes.
SELECT rental_date, customer_id
FROM rental
WHERE customer_id = 7
AND EXTRACT(YEAR FROM rental_date) = 2005
AND EXTRACT(MONTH FROM rental_date) = 5;
-- or
SELECT rental_date, customer_id
FROM rental
WHERE customer_id = 7
AND rental_date BETWEEN '2005-05-01' AND '2005-05-31';

--3 Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”
SELECT payment_id, payment_date, amount
FROM payment;

--4 Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0.
SELECT title, rental_rate
FROM film
WHERE release_year = 2006
AND rental_rate > 4.0;

--5 Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas,
--si éstas pueden ser nulas, y su tipo de dato correspondiente.
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE,
    COALESCE(NUMERIC_PRECISION, CHARACTER_MAXIMUM_LENGTH) AS column_length,
    COLUMN_DEFAULT
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'public'
ORDER BY 
    TABLE_NAME,
    ORDINAL_POSITION;

--6 Realiza consultas SQL a varias tablas relacionadas logrando mostrar datos, sin presentar errores.
SELECT ac.actor_id ,ac.first_name, ac.last_name, fi.title
FROM film_actor fa
JOIN actor ac ON fa.actor_id = ac.actor_id
JOIN film fi ON fa.film_id = fi.film_id
WHERE ac.actor_id = 1;

--7 Hace uso de sentencias de agrupación, logrando resolver un problema planteado, sin presentar errores
SELECT
    CASE
        WHEN "length" < 60 THEN '< 60'
        WHEN "length" BETWEEN 60 AND 90 THEN '60 to 90 inclusive'
        WHEN "length" BETWEEN 91 AND 120 THEN '91 to 120 inclusive'
        ELSE '> 120'
    END AS minutes_category,
    COUNT(*) AS movies_count
FROM film
GROUP BY minutes_category;