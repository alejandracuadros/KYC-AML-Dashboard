# CFG-Group-project-group-3

Automataed Eligibility and Compliance Checker

Project Description
This project is an automated system designed to evaluate startups applying to MOgan Stanley`s Inclusive Venture Lab. It ensures they meet regulatory and eligibility requirements, including:
- Anti - Money Laudering (AML) complianc
- Politically Exposed Persons (PEP) checks
- Eligibility criteria based on funding stage, diversity, sustainability

The program includes:
- SQL database integration for structured data storage.
- Compliance reporting for Morgan Stanley analysts.
- A frontend dashboboard for user interaction.

Objectives:

1. Automate the eligibility and compliance checking process
2. Identify startups at high risk for AML violations or other compliance issues.
3. Provide investments analysts with clear and actionable compliance reports.

Deliverables

SQL Database: Includes tables for startups, founders, high-risk countries and PEPS.
Python Scripts: Eligibility and AML compliance checks, Error handling and validation, report generation.

Frontend Dashboard: Displays compliance results and provides interaction for analysts and startups.

PEP and High-Risk Third Countries Integration: Startups indicate if their founders or high manageral personnel and their close relatives are PEPs. Or if the startup is set up or operating in a high-risk third country.

Setup Instructions:

- Python 3.x above
- Flask
- MySQL
- Python library: requirements

PEP handling 

Politically Exposed Persons (PEPs) includes individuals in prominent goverment positions, state-owned enterprises, or high-ranking military roles and immediate family members (spouses, children, parents, siblings, who may also present heightened compliance risks).
Implementations:
During startup registration, user indicate PEP status, and this information is accessed, stored and factored into the compliancecheck.

Country Handling

During registration it should be identified if the founder/CEO is from a high-risk country, check if the startup is based in a high-risk country and if the startup operates or not in a high-risk country.

Frontend for startups

Allows startups to register and input their data such as PEP status, operational countries.
In here is possible to receive immediate results and eligibility feedback and flag any isssues with their application.

Frontend for Analysts
Provides analysts with detailed access to all compliance data for decision-making, including advanced tools for risk assessment and reporting.
Here the anaysts can view the PEP statuses, flagged countries, risk scores. 
And generating  report in formats like PDF or CVS for external use, also allows to add notes or comments to individual startup profiles, while highlighting startups with high-risk scores or incomplete compliance.
It can have a restrict access to authorized analysts.

Data Privacy and GDPR compliance
Even thou this is a student project, it will adhere to GDPR requirements to ensure the secure and lawful handling of personal data. 

Directory Structure

project_root/
#SQL schema
├── sql/
│   ├── create_tables.sql      
│   ├── insert_data.sql        
│   ├── queries.sql           
 # High-risk country data and # Placeholder for PEPs

├── data/
│   ├── high_risk_countries.txt 
│   └── pep_list_placeholder.txt

# Requirements and objectives

├── docs/
│   ├── requirements.md         
│   └── compliance_guidelines.pdf
# Eligibility checks, AML checks connections with SQL
├── scripts/
│   ├── eligibility_checks.py  
│   ├── aml_compliance.py       
│   ├── database_connector.py   
│   ├── app.py        
# Frontend for startups
├── frontend/ # Frontend components 
│ ├── startup/ │ 
│ ├── register.html 
│ │ ├── status.html

# Frontend for analysts showing the startup profile 

│ ├── analyst/│ 
│ ├── dashboard.html # Analyst dashboard to view startups │ 
│ ├── profile.html 

#test eligibility and AML logic          
├── tests/
│   ├── test_eligibility.py     
│   └── test_aml.py        
#sample report     
└── reports/
    └── compliance_report.pdf  


