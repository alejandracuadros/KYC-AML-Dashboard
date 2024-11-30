CREATE DATABASE regulatory_compliance;
USE regulatory_compliance;

CREATE TABLE startups(
startup_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR (255) NOT NULL,
country VARCHAR (255) NOT NULL,
founder_name  VARCHAR (255) NOT NULL, 
industry VARCHAR (255),
funding_stage VARCHAR (255),
is_sustainable BOOLEAN
);
