# KYC/AML Regulatory Compliance Dashboard

## Project Description
This project is an automated system designed to evaluate startups applying to Morgan Stanley's Inclusive Venture Lab. 
It ensures they meet regulatory and eligibility requirements, including:
- Anti - Money Laundering (AML) compliance
- Politically Exposed Persons (PEP) checks
- Eligibility criteria based on funding stage, diversity, sustainability

### The program includes:
- SQL database integration for structured data storage.
- Compliance reporting for Morgan Stanley analysts.
- A frontend dashboard for user interaction.

### Objectives:

1. Automate the eligibility and compliance checking process
2. Identify startups at high risk for AML violations or other compliance issues.
3. Provide investments analysts with clear and actionable compliance reports.

### Deliverables

- SQL Database: Includes tables for startups, founders, high-risk countries and PEPS.
- Python Scripts: Eligibility and AML compliance checks, Error handling and validation, report generation.
- Frontend Dashboard: Displays compliance results and provides interaction for analysts and startups.
- PEP and High-Risk Third Countries Integration: Startups indicate if their founders or high managerial personnel and their close relatives are PEPs. 
Or if the startup is set up or operating in a high-risk third country.

### Setup Instructions:

1. Install Python 3.x above.
2. Install the required libraries from the `requirements.txt` file using the command below:
   `pip install -r requirements.txt`

3. Ensure you have the following dependencies:
   - Flask
   - MySQL
   - Pandas
   - Streamlit
4. Set up the database using the SQL scripts.
   - Execute the next SQL Scripts:
     - [regulatory_compliance_data.sql](regulatory_compliance_data.sql)
   
   - You can also run the next one to populate the DB
     - [database_population.sql](database_population.sql)
5. The Startup is able to access the Submission page and submit all their personal data and documents requested for the system. [app.py](app.py)
6. The analyst could check this data through dashboards, metrics, graphs and reports that can download for their convenience. [dashboard.py](dashboard.py)
7. Streamlit is the tool that helped us to execute the project.
8. Test been already elaborated during the execution of it. It's safe and easy to use, for the client and for the company.
   
   
## PEP handling 

Politically Exposed Persons (PEPs) includes individuals in prominent government positions, state-owned enterprises, or high-ranking military roles and immediate family members (spouses, children, parents, siblings, etc) who may also present heightened compliance risks.

### Implementations:
During startup registration, user indicate PEP status, and this information is accessed, stored and factored into the compliance check.

### Country Handling

During registration, it should identify if the founder/CEO is from a high-risk country, check if the startup is based in a high-risk country and if the startup operates in a high-risk country.

### Frontend for startups

- Startups can register and input their data such as PEP status, operational countries.
- Startups can receive immediate results and eligibility feedback and flag any issues in their application.

### Frontend for Analysts
- Analysts can have detailed access to all compliance data for decision-making, including KPIs and graphics for risk assessment and reporting.
- Analysts can view the PEP statuses, flagged countries, risk scores. 
- Generate  report in formats like PDF or CVS for external use.
- Only accessible to only authorized analysts.

### Data Privacy and GDPR compliance
Even though this is a student project, it will adhere to GDPR requirements to ensure the secure and lawful handling of personal data. 


## Project Developers:
- Alejandra Cuadros Rivas
- Ana Carolina Bergamasco Perez
- Clara Maria Barbosa Teodoro
- Lilla Horváth
- Bruna Rocha
- Chiamaka Maria-Goretti Adinnu




