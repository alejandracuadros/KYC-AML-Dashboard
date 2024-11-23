CREATE DATABASE PEP_Identification;
USE PEP_Identification;

-- since we can not affort the PEP API, due to its high costs, for the sake of this project
-- we create a database with fictious information, to a better understand of MS risk analysts and the
-- creation of the final report

-- PEPs informations storage
CREATE TABLE pep_individuals(
id INT AUTO_INCREMENT PRIMARY KEY,
full_name VARCHAR(150) NOT NULL,
job_title VARCHAR(150),
country VARCHAR(100),
class VARCHAR(100), -- specify the goverment body type eg: goverment, military, or judiciary
date_of_birth DATE,
last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

-- Informations about the entities associated with PEPs.

CREATE TABLE pep_and_organization_association(
id INT AUTO_INCREMENT PRIMARY KEY,
pep_id INT NOT NULL,
organization_name VARCHAR(200),
relationship_type VARCHAR(100), -- eg:ownership, partnership
country VARCHAR(100), -- country whre is the owrganization
FOREIGN KEY (pep_id) REFERENCES pep_individuals(id) ON DELETE CASCADE);

-- pep_watchlist to connect pep_individuals tables to specific high-risks watchlists
-- and track the risk level and the date that the PEP was added to the watchlist
CREATE TABLE pep_watchlist(
id INT AUTO_INCREMENT PRIMARY KEY,
pep_id INT NOT NULL,
watchlist_name VARCHAR(100) NOT NULL,
risk_level ENUM('Low', 'Medium', 'High') NOT NULL);








