-- Active: 1725460995925@@127.0.0.1@5432@tools-rent
SELECT * FROM companies LIMIT 100

INSERT INTO companies VALUES ('12345678-9','Apple','Loop 1',55516774,'apple@icloud.com','www.apple.com');

INSERT INTO tools VALUES (DEFAULT,'Macbook Pro',1000);
INSERT INTO tools VALUES (DEFAULT,'iPhone 13',800);
INSERT INTO tools VALUES (DEFAULT,'iPad Pro',600);
INSERT INTO tools VALUES (DEFAULT,'Apple Watch',400);
INSERT INTO tools VALUES (DEFAULT,'AirPods',200);

INSERT INTO clients VALUES ('98765432-1','Samsung','Loop 2','samsung@gmail.com',55516775);
INSERT INTO clients VALUES ('12345678-9','NVIDIA','Loop 3','nvidia@gmail.com',55516776);
INSERT INTO clients VALUES ('98765432-7','AMD','Loop 4','amd@gmail.com',55516777);

DELETE FROM clients
WHERE "name" = 'AMD';

DELETE FROM tools
WHERE "tool_id" = 1;

INSERT INTO rentals VALUES (DEFAULT, '2022-10-10', 4, 100,'doesnt pay if stolen',2,'98765432-1');
INSERT INTO rentals VALUES (DEFAULT, '2022-10-10', 6, 200,'doesnt pay if broke',3,'98765432-1');
INSERT INTO rentals VALUES (DEFAULT, '2022-10-10', 8, 300,'doesnt pay if lost',4,'12345678-9');
INSERT INTO rentals VALUES (DEFAULT, '2022-10-10', 10, 400,'doesnt pay if stolen',5,'12345678-9');

UPDATE clients
SET "email"='samsung@samsung.com'
WHERE "name" = 'Samsung';

SELECT * FROM tools;

SELECT * FROM rentals ren
JOIN clients cli ON ren.client_rut = cli.rut
WHERE cli.name = 'Samsung';

SELECT * FROM clients cli
WHERE "name" LIKE '%a%'
OR  "name" LIKE '%A%';

SELECT too.name FROM tools too
WHERE "tool_id" = 2;

UPDATE rentals
SET "date" = '2020-01-15'
WHERE "rent_id" = 1;

UPDATE rentals
SET "date" = '2020-01-15'
WHERE "rent_id" = 3;

SELECT * FROM rentals
WHERE "date" BETWEEN '2020-01-01' AND '2020-01-31';