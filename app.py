import streamlit as st

# Function to inject custom CSS
def inject_css():
        st.markdown(
            """
            <style>
            
            /* Change the header color */
            .stAppHeader {
                background-color: #021021;
                font-family: 'Arial', sans-serif;
            }
            
            /* Change the main background color */
            .stApp {
                background-color: #021021;
                font-family: 'Arial', sans-serif;  
            }
            
            /* Change sidebar background color */
            .stSidebar { 
                background-color: #05254F; 
                color: white ; 
                font-family: 'Arial', sans-serif;
            }
    
            /* Customize submit button */
            button {
                background-color: #073470 !important;
                color: white !important;
                font-family: 'Arial', sans-serif; 
            }
            button:hover {
                background-color: #135F91 !important; 
            }
    
            </style>
            """,
            unsafe_allow_html=True
        )

    # Inject CSS
inject_css()

# Page Title
st.title("Morgan Stanley Inclusive Venture Lab Submission")
st.subheader("Welcome")

st.markdown(
    """
    Thank you for your interest in joining the Morgan Stanley Inclusive Venture Lab (MSIVL).

    This portal will guide you through the process of submitting your startup’s information for evaluation. Our automated system will assess your **eligibility**, **compliance**, and **alignment with our sustainability goals** and **anti-money laundering (AML)** requirements.

    Please ensure you have all the necessary details and documents ready before starting the submission process.
    """,
    unsafe_allow_html=True,
)

# Sidebar menu
st.sidebar.title("Navigate through sections:")

# Use session state to store the selected section
if "selected_section" not in st.session_state:
    st.session_state["selected_section"] = "Startup Information"  # Default section

# Sidebar buttons to navigate between sections
if st.sidebar.button("Startup Information"):
    st.session_state["selected_section"] = "Startup Information"
if st.sidebar.button("Founder Details"):
    st.session_state["selected_section"] = "Founder Details"
if st.sidebar.button("Business Information"):
    st.session_state["selected_section"] = "Business Information"
if st.sidebar.button("Compliance and Screening Data"):
    st.session_state["selected_section"] = "Compliance and Screening Data"
if st.sidebar.button("Sustainability Metrics"):
    st.session_state["selected_section"] = "Sustainability Metrics"
if st.sidebar.button("Additional Documents"):
    st.session_state["selected_section"] = "Additional Documents"

# Get the selected section from session state
selected_section = st.session_state["selected_section"]

# Initialize session state for inputs---
for field in [
    "startup_name",  # Startup Information
    "registration_number",
    "country_of_incorporation",
    "date_of_incorporation",
    "full_name",  # Founder Details
    "nationality",
    "gender",
    "role",
    "contact",
    "industry",  # Business Information
    "last_year_revenue",
    "current_projected_revenue",
    "description_prod_serv",
    "amount_raised",
    "investors",
    "board_member_names",  # Compliance and Screening Data
    "criminal_record_declaration",
    "proof_of_aml_compliance",
    "bank_account_verification_doc",
    "sustainability_goals",  # Sustainability Metrics
    "environment_impact_description",
    "social_impact_contributions",
    "incorporation_proof",  # Additional Documents
    "financial_statements",
]:
    if field not in st.session_state:
        # Initialize empty strings or appropriate defaults for each field
        if field in ["proof_of_aml_compliance", "bank_account_verification_doc", "incorporation_proof",
                     "financial_statements"]:
            st.session_state[field] = None  # File uploaders default to None
        else:
            st.session_state[field] = ""

# Selected section display
if selected_section == "Startup Information":
    st.subheader("Startup Information")

    st.session_state.startup_name = st.text_input(
        "Startup Name",
        value = st.session_state.startup_name,
        placeholder="Enter your startup's official name"
    )
    st.session_state.registration_number = st.text_input(
        "Registration Number",
        value = st.session_state.registration_number,
        placeholder="Provide the registration ID"
    )
    st.session_state.country_of_incorporation = st.text_input(
        "Country of Incorporation",
        value = st.session_state.country_of_incorporation,
        placeholder="Country where the startup is registered"
    )
    st.session_state.date_of_incorporation = st.date_input(
        "Date of Incorporation",
        value=st.session_state.date_of_incorporation
    )

    # startup_name = st.text_input("Startup Name", placeholder="Enter your startup's official name")
    # registration_number = st.text_input("Registration Number", placeholder="Provide the registration ID")
    # country_of_incorporation = st.text_input("Country of Incorporation", placeholder="Country where the startup is registered")
    # date_of_incorporation = st.date_input("Date of Incorporation")

elif selected_section == "Founder Details":
    st.subheader("Founder Details")

    st.session_state.full_name = st.text_input(
        "Full Name",
        value = st.session_state.full_name,
        placeholder="Enter full name of the founder"
    )
    st.session_state.nationality = st.text_input(
        "Nationality",
        value = st.session_state.nationality,
        placeholder="Nationality of the founder"
    )
    st.session_state.gender = st.selectbox(
        "Gender", ["Male", "Female", "Other"],
        index=["Male", "Female", "Other"].index(st.session_state.gender or "Male")
    )
    st.session_state.role = st.text_input(
        "Role",
        value = st.session_state.role,
        placeholder="Role in the company"
    )
    st.session_state.contact = st.text_input(
        "Contact",
        value = st.session_state.contact,
        placeholder="Email or phone"
    )


    # full_name = st.text_input("Full Name", placeholder="Enter full name of the founder")
    # nationality = st.text_input("Nationality", placeholder="Nationality of the founder")
    # gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    # role = st.text_input("Role", placeholder="Role in the company")
    # contact = st.text_input("Contact", placeholder="Email or phone")

elif selected_section == "Business Information":
    st.subheader("Business Information")

    st.session_state.industry = st.selectbox(
        "Industry/Technology Focus",
        ["Choose one", "Robotics", "AI", "Fintech", "Healthcare", "Education", "Agriculture", "Transportation",
         "Energy", "Manufacturing"],
        index=["Choose one", "Robotics", "AI", "Fintech", "Healthcare", "Education", "Agriculture", "Transportation",
               "Energy", "Manufacturing"].index(
            st.session_state.industry or "Choose one"
        ),
    )

    st.subheader("Revenue Generation:")

    st.session_state.last_year_revenue = st.text_input(
        "Last Year’s Revenue",
        value =  st.session_state.last_year_revenue,
        placeholder="Enter revenue for the last year"
    )
    st.session_state.current_projected_revenue = st.text_input(
        "Projected Revenue",
        value = st.session_state.current_projected_revenue,
        placeholder="Enter projected revenue for this year"
    )
    st.session_state.description_prod_serv = st.text_area(
        "Description of Products/Services",
        value = st.session_state.description_prod_serv,
        placeholder="Briefly describe your offerings"
    )

    st.subheader("Funding Information:")
    st.session_state.amount_raised = st.text_input(
        "Amount raised",
        value = st.session_state.amount_raised,
        placeholder="Enter amount raised in EUR"
    )

    st.session_state.investors = st.text_input(
        "Investors",
        value = st.session_state.investors,
        placeholder="If applicable, enter name of investors"
    )

    # industry = st.selectbox("Industry/Technology Focus", ["Choose one", "Robotics", "AI", "Fintech", "Healthcare", "Education", "Agriculture", "Transportation", "Energy", "Manufacturing"])
    # last_year_revenue = st.text_input("Last year’s revenue", placeholder="Enter revenue for the last year")
    # current_projected_revenue = st.text_input("Projected revenue for the current year", placeholder="Enter projected revenue for this year")
    # description_prod_serv = st.text_input("Description of Products/Services", placeholder="Briefly describe your offerings")
    # amount_raised = st.text_input("Amount raised", placeholder="Enter amount raised in EUR")
    # investors = st.text_input("Investors", placeholder="If applicable, enter name of investors")

elif selected_section == "Compliance and Screening Data":
    st.subheader("Compliance and Screening Data")

    st.session_state.board_member_names = st.text_input(
        "Board Member Names",
        value = st.session_state.board_member_names,
        placeholder="Enter names of key board members separated by commas"
    )
    st.session_state.criminal_record_declaration = st.selectbox(
        "Criminal Record Declaration",
        ["No records", "Records exist"],
        index=["No records", "Records exist"].index(st.session_state.criminal_record_declaration or "No records"),
    )

    st.subheader("AML-Related Documents")

    st.session_state.proof_of_aml_compliance = st.file_uploader(
        "Proof of AML Compliance",
        type=["pdf", "docx"])
    st.session_state.bank_account_verification_doc = st.file_uploader(
        "Bank Account Verification Document",
        type=["pdf"])
    # board_member_names = st.text_input("Board Member Names", placeholder="Enter names of key board members separated by comma (,)")
    # criminal_record_declaration = st.selectbox("Criminal Record Declaration", ["No records", "Records exist"])
    # proof_of_aml_compliance = st.file_uploader("Proof of AML Compliance", type=["pdf", "docx"])
    # bank_account_verification_doc = st.file_uploader("Bank Account Verification Document", type=["pdf"])

elif selected_section == "Sustainability Metrics":
    st.subheader("Sustainability Metrics")

    st.session_state.sustainability_goals = st.selectbox(
        "Sustainability Goals",
        ["Carbon Reduction", "Waste Management", "Energy Efficiency"],
        index=["Carbon Reduction", "Waste Management", "Energy Efficiency"].index(
            st.session_state.sustainability_goals or "Carbon Reduction"
        ),
    )
    st.session_state.environment_impact_description = st.text_input(
        "Environmental Impact Description",
        value = st.session_state.environment_impact_description,
        placeholder="Describe your sustainability efforts",
    )
    st.session_state.social_impact_contributions = st.text_input(
        "Social Contributions",
        value = st.session_state.social_impact_contributions,
        placeholder="Outline your contributions to social causes",
    )
    # sustainability_goals = st.selectbox("Sustainability Goals", ["Carbon Reduction", "Waste Management", "Energy Efficiency"])
    # environment_impact_description = st.text_input("Environmental Impact Description", placeholder="Describe your sustainability efforts")
    # social_impact_contributions = st.text_input("Social Contributions", placeholder="Outline your contributions to social causes")

elif selected_section == "Additional Documents":
    st.subheader("Additional Documents")
    st.session_state.incorporation_proof = st.file_uploader(
        "Proof of Incorporation",
        type=["pdf"])
    st.session_state.financial_statements = st.file_uploader(
        "Financial Statements",
        type=["pdf"])

    # incorporation_proof = st.file_uploader("Proof of Incorporation", type=["pdf"])
    # financial_statements = st.file_uploader("Financial Statements", type=["pdf"])

# Submit button
if st.button("Submit"):
    st.success("Form submitted successfully!")


