CREATE DATABASE eu_countries_blacklist;
USE  eu_countries_blacklist;


-- This database has the necessary information regarding the EU Third- Coutries blaclklist
-- according to the AML/CFT (anti-money laundering and counter-terrorism financing) framewo ks


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
('Gibraltar',
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
('Vietnam')
;

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

