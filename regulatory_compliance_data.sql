CREATE DATABASE regulatory_compliance;
USE regulatory_compliance;

CREATE TABLE high_risk_countries(
ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
country_name VARCHAR(100));

INSERT INTO high_risk_countries (country_name)
VALUES
('Afghanistan'),
('Barbados'),
('Burkina Faso'),
('Cameroon'),
('Democratic Republic of Congo'),
('Gibraltar'),
('Haiti'),
('Jamaica'),
('Mali'),
('Mozambique'),
('Myanmar'),
('Nigeria'),
('Panama'),
('Philippines'),
('Senegal'),
('South Africa'),
('South Sudan'),
('Syria'),
('Tanzania'),
('Trinidad and Tobago'),
('Uganda'),
('United Arab Emirates'),
('Vanuatu'),
('Vietnam');

CREATE TABLE country_seeking_tech_assitance(
ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
country_name VARCHAR(100));

INSERT INTO country_seeking_tech_assitance(country_name)
VALUES
('Iran')
;

CREATE TABLE countries_with_ongoing_risks(
ID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
country_name VARCHAR(100));

INSERT INTO countries_with_ongoing_risks(country_name)
VALUES
('Democratic People`s of Korea - DPRK')
;


CREATE TABLE pep_individuals(
pep_id INT AUTO_INCREMENT PRIMARY KEY,
full_name VARCHAR(150) NOT NULL,
job_title VARCHAR(150),
country VARCHAR(100),
class VARCHAR(100), -- specify the goverment body type eg: goverment, military, or judiciary
date_of_birth DATE,
last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

-- Informations about the entities associated with PEPs.

CREATE TABLE pep_and_organization_association(
pep_id INT NOT NULL,
organization_name VARCHAR(200),
relationship_type VARCHAR(100), -- eg:ownership, partnership
country VARCHAR(100), -- country whre is the owrganization
FOREIGN KEY (pep_id) REFERENCES pep_individuals(pep_id) ON DELETE CASCADE);

CREATE TABLE startups(
startup_id INT PRIMARY KEY,
startup_name VARCHAR (255) NOT NULL,
country VARCHAR (255) NOT NULL,
date_of_incorporation DATE,
company_size VARCHAR (50),
employees INT 
);

CREATE TABLE founders_details(
passport_id  VARCHAR (15) NOT NULL PRIMARY KEY,
full_name VARCHAR (255) NOT NULL,
date_of_birth DATE,
nationality VARCHAR (50),
birth_place VARCHAR (50),
residence_place VARCHAR (50),
gender VARCHAR (20),
phone_number VARCHAR (50),
email VARCHAR (255),
startup_id INT,
role_in_startup VARCHAR (50),
FOREIGN KEY (startup_id) REFERENCES startups(startup_id)
);

CREATE TABLE startup_profile(
startup_id INT PRIMARY KEY,
industry VARCHAR (255),
last_year_revenue FLOAT,
current_projected_revenue FLOAT,
next_year_revenue FLOAT,
amount_raised FLOAT,
FOREIGN KEY (startup_id) REFERENCES startups(startup_id)
);

CREATE TABLE investors (
startup_id INT,
investor_name VARCHAR (255) NOT NULL,
passport_id VARCHAR (15) NOT NULL,
FOREIGN KEY (startup_id) REFERENCES startups(startup_id)
);

CREATE TABLE board_members (
startup_id INT,
member_name VARCHAR (255) NOT NULL,
passport_id VARCHAR (15) NOT NULL,
FOREIGN KEY (startup_id) REFERENCES startups(startup_id)
);

CREATE TABLE sustainability (
startup_id INT,
goals VARCHAR (255),
impact VARCHAR (255),
social_contribution VARCHAR (255),
FOREIGN KEY (startup_id) REFERENCES startups(startup_id)
);
