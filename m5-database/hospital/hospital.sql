-- Active: 1725460995925@@127.0.0.1@5432@hospital
CREATE DATABASE hospital;

BEGIN;
CREATE TABLE IF NOT EXISTS patients (
    "patient_id" SERIAL,
    "first_name" TEXT,
    "last_name" TEXT,
    "date_of_birth" DATE,
    "physical_sex" CHAR(1),
    PRIMARY KEY ("patient_id")
);
CREATE TABLE IF NOT EXISTS doctors (
    "doctor_id" SERIAL,
    "first_name" TEXT,
    "last_name" TEXT,
    "specialty" VARCHAR(50),
    PRIMARY KEY ("doctor_id")
);
CREATE TABLE IF NOT EXISTS appointments (
    "appointment_id" SERIAL,
    "patient_id" INT,
    "doctor_id" INT,
    "date" DATE,
    PRIMARY KEY ("appointment_id")
);
CREATE TABLE IF NOT EXISTS treatments (
    "treatment_id" SERIAL,
    "appointment_id" INT,
    "description" TEXT,
    "cost" NUMERIC(10, 2),
    PRIMARY KEY ("treatment_id")
);
ALTER TABLE IF EXISTS appointments
    ADD CONSTRAINT fk_appointments_patients_patient_id FOREIGN KEY (patient_id)
    REFERENCES patients (patient_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS appointments
    ADD CONSTRAINT fk_appointments_doctors_doctor_id FOREIGN KEY (doctor_id)
    REFERENCES doctors (doctor_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS treatments
    ADD CONSTRAINT fk_treatments_appointments_appointment_id FOREIGN KEY (appointment_id)
    REFERENCES appointments (appointment_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
END;

BEGIN;
INSERT INTO patients ("first_name", "last_name", "date_of_birth", "physical_sex") VALUES
('Juan', 'Pérez', '1985-06-15', 'M'),
('Ana', 'Gómez', '1990-04-22', 'F'),
('Carlos', 'Ruiz', '1978-11-30', 'M');
INSERT INTO doctors ("first_name", "last_name", "specialty") VALUES
('Jorge', 'Kaplan', 'Cardiología'),
('Rick' ,'Sánchez', 'Pediatría'),
('Francisca', 'López', 'Ginecología');
INSERT INTO appointments ("patient_id", "doctor_id", "date")
VALUES (1, 1, '2024-09-15'),
(2, 2, '2024-09-16'),
(3, 3, '2024-09-17');
INSERT INTO treatments ("appointment_id", "description", "cost") VALUES
(1, 'Consulta general y examen físico', 150.00),
(2, 'Revisión pediátrica y vacunas', 200.00),
(3, 'Chequeo ginecológico y ecografía', 250.00);
END;

--1 INNER JOIN Show all patients with their doctor's information and the treatment received:
--2 LEFT JOIN Show all patients and, if they have, the treatment received and the doctor's name:
--3 RIGHT JOIN Show all treatments and, if they exist, the patient's and doctor's information:
--4 CROSS JOIN Show all possible combinations of patients and doctors:

--5 UNION: Show all patient and doctor names (without duplicates):
--6 INTERSECT: Show the names that are in both the patients table and the doctors table (although in this case, we shouldn't have common names between patients and doctors):
--7 EXCEPT (equivalent to MINUS in PostgreSQL): Show the names of patients that are not in the doctors table (in this case, it should show all patients because we don't share names between the tables):
--8 EXTRACT: Show the patients whose birthday is in the same month as the current date:

--9 UNION: with Patient and Appointment Data
--Show all patient names and appointment IDs:
--10 INTERSECT: with Patient and Doctor Data
-- Show names that are found in both patients and doctors (we expect this to be empty if there are no common names):
--11 EXCEPT: with Patient and Treatment Data
--Show names of patients who do not have a registered treatment (this assumes that all patients with appointments have registered treatments, so it should be empty):
