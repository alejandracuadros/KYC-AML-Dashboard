# CFG-Group-project-group-3

Automated Eligibility and Compliance Checker

Project Description
This project is an automated system designed to evaluate startups applying to Morgan Stanley's Inclusive Venture Lab. It ensures they meet regulatory and eligibility requirements, including:
- Anti - Money Laundering (AML) compliance
- Politically Exposed Persons (PEP) checks
- Eligibility criteria based on funding stage, diversity, sustainability

The program includes:
- SQL database integration for structured data storage.
- Compliance reporting for Morgan Stanley analysts.
- A frontend dashboard for user interaction.

Objectives:

1. Automate the eligibility and compliance checking process
2. Identify startups at high risk for AML violations or other compliance issues.
3. Provide investments analysts with clear and actionable compliance reports.

Deliverables

- SQL Database: Includes tables for startups, founders, high-risk countries and PEPS.
- Python Scripts: Eligibility and AML compliance checks, Error handling and validation, report generation.
- Frontend Dashboard: Displays compliance results and provides interaction for analysts and startups.
- PEP and High-Risk Third Countries Integration: Startups indicate if their founders or high manageral personnel and their close relatives are PEPs. Or if the startup is set up or operating in a high-risk third country.

Setup Instructions:

1. Install Python 3.x above.
2. Install the required libraries from the `requirements.txt` file using the command below:
   `pip install -r requirements.txt`
3. Ensure you have the following dependencies:
   - Flask
   - MySQL
   - Pandas
   - Streamlit
4. Set up the database manually using the provided SQL scripts:
   
   4.1. Start by executing the SQL script located in the file `regulatory_compliance_data.sql`.
   
   4.2. Next, execute the SQL script located in the file `database_population.sql`.

Running the project:

- To run the *Client Interface*, open the terminal and use the command:  `streamlit run app.py`

- To run the *Analyst Dashboard*, open the terminal and use the command: `streamlit run dashboard.py`

Note: Login credentials for both interfaces are stored in the login_credentials.csv file.


PEP handling 

Politically Exposed Persons (PEPs) includes individuals in prominent government positions, state-owned enterprises, or high-ranking military roles and immediate family members (spouses, children, parents, siblings, etc) who may also present heightened compliance risks.

Implementations:
During startup registration, user indicate PEP status, and this information is accessed, stored and factored into the compliance check.

Country Handling

During registration, it should identify if the founder/CEO is from a high-risk country, check if the startup is based in a high-risk country and if the startup operates in a high-risk country.

Frontend for startups

- Startups can register and input their data such as PEP status, operational countries.
- Startups can receive immediate results and eligibility feedback and flag any issues in their application.

Frontend for Analysts
- Analysts can have detailed access to all compliance data for decision-making, including advanced tools for risk assessment and reporting.
- Analysts can view the PEP statuses, flagged countries, risk scores. 
- Generate  report in formats like PDF or CVS for external use.
- Analysts can also add notes or comments to individual startup profiles, while highlighting startups with high-risk scores or incomplete compliance.
- It can have access restrictions to only authorized analysts.

Data Privacy and GDPR compliance
Even though this is a student project, it will adhere to GDPR requirements to ensure the secure and lawful handling of personal data. 
