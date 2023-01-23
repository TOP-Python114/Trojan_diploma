BEGIN;
--
-- Create model Vacancy
--
CREATE TABLE "site_vacancy_vacancy" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Position" varchar(40) NOT NULL,
    "Salary" decimal NOT NULL,
    "Work_schedule" varchar(40) NOT NULL,
    "responsibilities" text NOT NULL,
    "requirements" text NOT NULL,
    "working_conditions" text NOT NULL
);

COMMIT;

