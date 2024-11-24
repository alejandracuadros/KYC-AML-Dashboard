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

-- Query to fetch all startups in high-risk countries
SELECT
s.startup_id,
s.name AS startup_name,
s.country AS startup_country, 
hrc.country_name AS high_risk_country
FROM 
regulatory_compliance.startups s 
JOIN 
eu_countries_blacklist.high_risk_countries hrc
ON s.country = hrc.country_name;

-- Query to fetch startups with pep founders
SELECT 
s.startup_id, 
s.name AS startup_name, 
s.founder_name AS founder_name,
p.full_name AS pep_name,
p.class AS pep_class,
p.country AS pep_country
FROM 
regulatory_compliance.startups s 
JOIN 
PEP_Identification.pep_individuals p 
ON s.founder_name = p.full_name;

-- Query to flag startups in high risk countries
SELECT 
s.startup_id, 
s.name AS startup_name,
CASE 
WHEN hrc.country_name IS NOT NULL THEN 'High-Risk Country'
WHEN p.full_name IS NOT NULL THEN 'PEP Founder'
ELSE 'Low Risk'
END AS risk_level
FROM 
regulatory_compliance.startups s 
JOIN
eu_countries_blacklist.high_risk_countries hrc
ON
s.country = hrc.country_name
JOIN 
PEP_Identification.pep_individuals p
ON
s.founder_name = p.full_name;