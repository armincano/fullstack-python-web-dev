--7. Listar todos los actores que aparecen en la película "Titanic",
--indicando el título de la película, año de estreno, director y todo el reparto.
SELECT ca.actor, mo.name, mo.release_year, mo.director FROM "movies" mo
JOIN "cast" ca ON mo.movie_id = ca.movie_id
WHERE mo.name = 'Titanic';

--8. Listar los 10 directores más populares,
--indicando su nombre y cuántas películas aparecen en el top 100.
SELECT mo.director, COUNT(*) AS movies_in_top_100 FROM movies mo
GROUP BY mo.director
ORDER BY 2 DESC
LIMIT 10;

--9. Indicar cuántos actores distintos hay.
SELECT * FROM "cast";
SELECT COUNT(DISTINCT(ca.actor)) AS distinct_actors FROM "cast" ca;

--10. Indicar las películas estrenadas entre los años 1990 y 1999 (ambos incluidos),
--ordenadas por título de manera ascendente.
SELECT mo.name, mo.release_year FROM movies mo
WHERE mo.release_year BETWEEN 1990 AND 1999
ORDER BY mo.release_year;

--11. Listar los actores de la película más nueva.
SELECT mo.name, ca.actor
FROM movies mo
JOIN "cast" ca ON mo.movie_id = ca.movie_id
WHERE mo.movie_id = (
	SELECT movie_id FROM movies
	WHERE release_year = (
		SELECT MAX(release_year) FROM movies
	)
	ORDER BY movie_id DESC
	LIMIT 1
);

--12. Inserte los datos de una nueva película solo en memoria,
--y otra película en el disco duro.
BEGIN;
CREATE SEQUENCE movies_id_seq;
ALTER TABLE movies
ALTER COLUMN movie_id SET DEFAULT nextval('movies_id_seq');
ALTER SEQUENCE movies_id_seq OWNED BY movies.movie_id;
SELECT setval('movies_id_seq', (SELECT MAX(movie_id) FROM movies));
COMMIT;

SELECT * FROM movies;
BEGIN;
INSERT INTO movies VALUES(DEFAULT, 'fake movie 1', 2022, 'Vicente Sabat');
ROLLBACK;

BEGIN;
INSERT INTO movies VALUES(DEFAULT, 'fake movie 2', 2024, 'Vicente Sabat');
COMMIT;

--13. Actualice 5 directores utilizando ROLLBACK.

--14. Inserte 3 actores a la película “Rambo” utilizando SAVEPOINT

--15. Elimina las películas estrenadas el año 2008 solo en memoria.

--16. Inserte 2 actores para cada película estrenada el 2001.

--17. Actualice la película “King Kong” por el nombre de “Donkey Kong”,
--sin efectuar cambios en disco duro.
