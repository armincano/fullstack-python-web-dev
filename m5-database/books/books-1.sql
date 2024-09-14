-- Active: 1725460995925@@127.0.0.1@5432@books-1
INSERT INTO publishers ("name") VALUES
('Anaya'),
('Andina'),
('S.M.');
INSERT INTO books ("title", "publisher_id") VALUES
('Don Quijote de La Mancha I',1),
('El principito',2),
('El príncipe',3),
('Diplomacia',3),
('Don Quijote de La Mancha II',1);

ALTER TABLE books
ADD COLUMN "author" TEXT;
ALTER TABLE books
ADD COLUMN "price" INTEGER;

BEGIN;
UPDATE books
SET "author" = 'Miguel de Cervantes', "price" = 150
WHERE book_id = 1;
UPDATE books
SET "author" = 'Antoine SaintExupery', "price" = 120
WHERE book_id = 2;
UPDATE books
SET "author" = 'Maquiavelo', "price" = 180
WHERE book_id = 3;
UPDATE books
SET "author" = 'Henry Kissinger', "price" = 170
WHERE book_id = 4;
UPDATE books
SET "author" = 'Miguel de Cervantes', "price" = 140
WHERE book_id = 5;
COMMIT;

ALTER TABLE books
ADD CONSTRAINT "books_price_check" CHECK ("price" > 0);
ALTER TABLE books
ALTER COLUMN "author" SET NOT NULL;
ALTER TABLE books
ALTER COLUMN "price" SET NOT NULL;

BEGIN;
INSERT INTO books (title, publisher_id, author, price) VALUES
('El arte de la guerra',3,'Sun Tzu',200),
('El arte de amar',2,'Erich Fromm',180);
COMMIT;

BEGIN;
DELETE FROM books
WHERE "publisher_id" = 2;
SELECT * FROM books;
ROLLBACK;

BEGIN;
UPDATE publishers
SET "name"='Mountain'
WHERE "name"='S.M.';
SAVEPOINT sm_to_mountain;
UPDATE publishers
SET "name"='Iberlibro'
WHERE "name"='Andina';
ROLLBACK TO sm_to_mountain;
COMMIT;