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
# st.sidebar.markdown("### Sections:")

# Create buttons for each section in the vertical menu
selected_section = None
if st.sidebar.button("Startup Information"):
    selected_section = "Startup Information"
if st.sidebar.button("Founder Details"):
    selected_section = "Founder Details"
if st.sidebar.button("Business Information"):
    selected_section = "Business Information"
if st.sidebar.button("Compliance and Screening Data"):
    selected_section = "Compliance and Screening Data"
if st.sidebar.button("Sustainability Metrics"):
    selected_section = "Sustainability Metrics"
if st.sidebar.button("Additional Documents"):
    selected_section = "Additional Documents"


# Default or selected section display
if selected_section == "Startup Information":
    st.subheader("Startup Information")
    # Input fields for Startup Information
    startup_name = st.text_input("Startup Name", placeholder="Enter your startup's official name")
    registration_number = st.text_input("Registration Number", placeholder="Provide the registration ID")
    country_of_incorporation = st.text_input("Country of Incorporation", placeholder="Country where the startup is registered")
    date_of_incorporation = st.date_input("Date of Incorporation")

elif selected_section == "Founder Details":
    st.subheader("Founder Details")
    full_name = st.text_input("Full Name", placeholder="Enter full name of the founder")
    nationality = st.text_input("Nationality", placeholder="Nationality of the founder")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    role = st.text_input("Role", placeholder="Role in the company")
    contact = st.text_input("Contact", placeholder="Email or phone")

elif selected_section == "Business Information":
    st.subheader("Business Information")

    industry = st.selectbox("Industry/Technology Focus", ["Choose one", "Robotics", "AI", "Fintech", "Healthcare", "Education", "Agriculture", "Transportation", "Energy", "Manufacturing"])

    st.subheader("Revenue Generation:")
    last_year_revenue = st.text_input("Last year’s revenue", placeholder="Enter revenue for the last year")
    current_projected_revenue = st.text_input("Projected revenue for the current year", placeholder="Enter projected revenue for this year")
    description_prod_serv = st.text_input("Description of Products/Services", placeholder="Briefly describe your offerings")

    st.subheader("Funding Information:")
    amount_raised = st.text_input("Amount raised", placeholder="Enter amount raised in EUR")
    investors = st.text_input("Investors", placeholder="If applicable, enter name of investors")

elif selected_section == "Compliance and Screening Data":
    st.subheader("Compliance and Screening Data")
    board_member_names = st.text_input("Board Member Names", placeholder="Enter names of key board members separated by comma (,)")
    criminal_record_declaration = st.selectbox("Criminal Record Declaration", ["No records", "Records exist"])
    st.subheader("AML-Related Documents")
    proof_of_aml_compliance = st.file_uploader("Proof of AML Compliance", type=["pdf", "docx"])
    bank_account_verification_doc = st.file_uploader("Bank Account Verification Document", type=["pdf"])

elif selected_section == "Sustainability Metrics":
    st.subheader("Sustainability Metrics")
    sustainability_goals = st.selectbox("Sustainability Goals", ["Carbon Reduction", "Waste Management", "Energy Efficiency"])
    environment_impact_description = st.text_input("Environmental Impact Description", placeholder="Describe your sustainability efforts")
    social_impact_contributions = st.text_input("Social Contributions", placeholder="Outline your contributions to social causes")

elif selected_section == "Additional Documents":
    st.subheader("Additional Documents")
    incorporation_proof = st.file_uploader("Proof of Incorporation", type=["pdf"])
    financial_statements = st.file_uploader("Financial Statements", type=["pdf"])

# Submit button
if st.button("Submit"):
    st.success("Form submitted successfully!")


