import datetime
from datetime import date
import pandas as pd
import streamlit as st
import pycountry
from add_to_database import DatabaseConnection  # type: ignore

db = DatabaseConnection()

# Login function
@st.cache_data
def load_credentials():
    return pd.read_csv("login_credentials.csv")


# Styling of the app
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


inject_css()

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

credentials = load_credentials()

# Check if the user is logged in
if not st.session_state["logged_in"]:

    # Login Page
    st.title("Morgan Stanley Inclusive Venture Lab")
    st.subheader("Login to the Portal")
    st.markdown("Please enter your credentials to access the Portal.")

    # Login Form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")


    # Login callback function
    def login_callback(username, password):
        if any((credentials['username'] == username) & (credentials['password'] == password)):
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password. Please try again.")


    # Login button with callback
    st.button("Login", on_click=login_callback, args=(username, password))

else:

    # Main Application

    st.title("Morgan Stanley Inclusive Venture Lab Submission")

    st.sidebar.title("Navigate through sections:")

    # We use session state to store the selected section
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = "Home"  # Default section

    # Home Page Content
    if st.session_state["selected_section"] == "Home":
        st.subheader("Welcome !")
        st.markdown(
            """
            This portal helps startups submit their information for evaluation as part of the 
            Morgan Stanley Inclusive Venture Lab initiative.

            ### Here's what you can do:
            - Navigate through the sections on the left sidebar.
            - Provide details about your startup, founders, and business operations.
            - Upload relevant documents to complete your submission.

            ### How to Use:
            1. Start with **Startup Information** to provide basic details.
            2. Proceed through each section using the sidebar menu.
            3. Submit your completed application by clicking the **Submit** button.

            **Ready to get started? Click on a section in the sidebar!**
            """,
            unsafe_allow_html=True,
        )

    # Sidebar buttons to navigate between sections
    if st.sidebar.button("Home"):
        st.session_state["selected_section"] = "Home"
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("Startup Information"):
        st.session_state["selected_section"] = "Startup Information"
    if st.sidebar.button("Founder Details"):
        st.session_state["selected_section"] = "Founder Details"
    if st.sidebar.button("Business Profile"):
        st.session_state["selected_section"] = "Business Profile"
    if st.sidebar.button("Risk and Compliance"):
        st.session_state["selected_section"] = "Risk and Compliance"
    if st.sidebar.button("Sustainability and Social Impact"):
        st.session_state["selected_section"] = "Sustainability and Social Impact"
    if st.sidebar.button("Additional Documents"):
        st.session_state["selected_section"] = "Additional Documents"
    st.sidebar.markdown("<br>", unsafe_allow_html=True)


    # Logout callback function
    def logout_callback():
        st.session_state["logged_in"] = False
        st.info("Logged out successfully.")


    # Logout button with callback
    st.sidebar.button("Log Out", on_click=logout_callback)

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
        "industry",  # Business Profile
        "last_year_revenue",
        "current_projected_revenue",
        "description_prod_serv",
        "amount_raised",
        "investors",
        "board_member_names",  # Risk and Compliance
        "criminal_record_declaration",
        "sustainability_goals",  # Sustainability and Social Impact
        "environment_impact_description",
        "social_impact_contributions",
        "incorporation_proof",  # Additional Documents
        "financial_statements",
    ]:
        if field not in st.session_state:
            # Initialize empty strings or appropriate defaults for each field
            if field in ["social_impact_contributions",
                         "incorporation_proof",
                         "financial_statements"]:
                st.session_state[field] = None
            else:
                st.session_state[field] = ""

    # Sections and their fields
    section_fields = {
        "Startup Information": [
            "startup_name",
            "registration_number",
            "country_of_incorporation",
            "date_of_incorporation",
            "company_size",
            "number_employees"
        ],
        "Founder Details": [
            "founders"
        ],
        "Business Profile": [
            "industry",
            "last_year_revenue",
            "current_projected_revenue",
            "next_year_revenue",
            "description_prod_serv",
            "amount_raised",
            "investors"
        ],
        "Risk and Compliance": [
            "board_members",
            "criminal_record_agreement",
        ],
        "Sustainability and Social Impact": [
            "sustainability_goals",
            "environment_impact_description",
            "social_impact_contributions"
        ],
        "Additional Documents": [
            "incorporation_proof",
            "financial_statements",
            "environmental_certifications"
        ]
    }

    # Initialize a dictionary to track missing fields
    if "missing_fields" not in st.session_state:
        st.session_state.missing_fields = {}

    # Selected section display
    if selected_section == "Startup Information":
        st.subheader("Startup Information")

        st.session_state.startup_name = st.text_input(
            "Startup Name",
            value=st.session_state.startup_name,
            placeholder="Enter your startup's official name"
        )
        st.session_state.registration_number = st.text_input(
            "Registration Number",
            value=st.session_state.registration_number,
            placeholder="Provide the registration ID of your startup"
        )

        # Load list of countries
        countries = [country.name for country in pycountry.countries]
        if "country_of_incorporation" not in st.session_state:
            st.session_state.country_of_incorporation = countries[0]

        st.session_state.country_of_incorporation = st.selectbox(
            "Country of Incorporation",
            countries,
            index=countries.index(st.session_state.country_of_incorporation)
            if st.session_state.country_of_incorporation in countries
            else 0
        )

        # Maximum date
        max_date = datetime.date.today() - datetime.timedelta(days=365)

        # Get the stored date or default to today
        default_date = st.session_state.get("date_of_incorporation", datetime.date.today())

        # Ensure the stored value is a valid datetime.date object
        if isinstance(default_date, str):
            try:
                default_date = datetime.date.fromisoformat(default_date)
            except ValueError:
                pass
            default_date = datetime.date.today()

        # Ensure default_date doesn't exceed max_date
        default_date = min(default_date, max_date)

        st.session_state.date_of_incorporation = st.date_input(
            "Date of Incorporation",
            value=default_date,
            max_value=max_date
        )

        # Company size options
        company_size_options = {"Micro Enterprise (Fewer than 10 employees)": (1, 9),
                                "Small Enterprise (10-49 employees)": (10, 49),
                                "Medium Enterprise (50-249 employees)": (50, 249),
                                "Large Enterprise (250 or more employees)": (250, float('inf'))
                                }

        if "company_size" not in st.session_state:
            st.session_state.company_size = list(company_size_options.keys())[0]
        if "number_employees" not in st.session_state:
            st.session_state.number_employees = 1

        # Company size selection
        st.session_state.company_size = st.selectbox(
            "Startup Size",
            options=list(company_size_options.keys()),
            index=list(company_size_options.keys()).index(st.session_state.company_size)
        )

        number_employees = st.number_input(
            "Number of Employees",
            min_value=1,
            step=1,
            value=st.session_state.number_employees,
            placeholder="Enter the number of employees of your startup"
        )

        st.session_state.number_employees = number_employees

        # Validate that the input matches the selected range
        min_employees, max_employees = company_size_options[st.session_state.company_size]
        if not (min_employees <= st.session_state.number_employees <= max_employees):
            st.error(f"Enter a number between {min_employees} and {max_employees}.")

        # Final Check
        # Fields for this section
        if st.button("Submit Section"):
            section_missing_fields = []

            # Validate the fields in this section
            for field in section_fields["Startup Information"]:
                if not st.session_state.get(field):
                    section_missing_fields.append(field.replace("_", " ").capitalize())

            # Update the missing fields dictionary
            st.session_state.missing_fields["Startup Information"] = section_missing_fields

            # Provide feedback
            if section_missing_fields:
                st.error("The following fields are missing in this section:\n\n" + "\n".join(
                    f"- {field}" for field in section_missing_fields))
            else:
                st.success("This section's data has been successfully validated!")

    elif selected_section == "Founder Details":

        # Initialize session state for founders
        if "founders" not in st.session_state:
            st.session_state.founders = [{"id": 1}]  # Start with one founder

        # Fetch country names using pycountry
        countries = ["Select a country"] + [country.name for country in pycountry.countries]
        roles = [
            "Founder",
            "Co-Founder",
            "Chief Executive Officer (CEO)",
            "Chief Technology Officer (CTO)",
            "Chief Operating Officer (COO)",
            "Chief Financial Officer (CFO)",
            "Chief Marketing Officer (CMO)",
            "Chief Product Officer (CPO)",
            "Chief Design Officer (CDO)",
            "Chief Data Officer (CDO)",
            "Chief Innovation Officer (CIO)",
            "Chief Sales Officer (CSO)",
            "Chief Growth Officer (CGO)",
            "Chief Legal Officer (CLO)"
        ]


        # Function to render the form for a founder
        def render_founder_form(founder):
            st.subheader(f"Founder {founder['id']} Details")

            founder["first_name"] = st.text_input(
                "First Name",
                value=founder.get("first_name", ""),
                placeholder="Enter the first name",
                key=f"first_name_{founder['id']}"
            )
            founder["last_name"] = st.text_input(
                "Last Name",
                value=founder.get("last_name", ""),
                placeholder="Enter the last name",
                key=f"last_name_{founder['id']}"
            )
            founder["date_of_birth"] = st.date_input(
                "Date of Birth",
                value=founder.get("date_of_birth", date(1990, 1, 1)),
                key=f"date_of_birth_{founder['id']}"
            )
            founder["passport_number"] = st.text_input(
                "Passport Number",
                value=founder.get("passport_number", ""),
                placeholder="Enter passport number",
                key=f"passport_number_{founder['id']}"
            )
            founder["nationality"] = st.selectbox(
                "Nationality",
                options=countries,
                index=countries.index(founder.get("nationality", "Select a country")) if founder.get(
                    "nationality") in countries else 0,
                key=f"nationality_{founder['id']}"
            )
            founder["place_of_birth"] = st.selectbox(
                "Place of Birth",
                options=countries,
                index=countries.index(founder.get("place_of_birth", "Select a country")) if founder.get(
                    "place_of_birth") in countries else 0,
                key=f"place_of_birth_{founder['id']}"
            )
            founder["place_of_residence"] = st.selectbox(
                "Place of Residence",
                options=countries,
                index=countries.index(founder.get("place_of_residence", "Select a country")) if founder.get(
                    "place_of_residence") in countries else 0,
                key=f"place_of_residence_{founder['id']}"
            )
            founder["gender"] = st.selectbox(
                "Gender",
                ["Male", "Female", "Other"],
                index=["Male", "Female", "Other"].index(founder.get("gender", "Male")),
                key=f"gender_{founder['id']}"
            )
            founder["phone_number"] = st.text_input(
                "Phone Number",
                value=founder.get("phone_number", ""),
                placeholder="Enter phone number",
                key=f"phone_number_{founder['id']}"
            )
            founder["email"] = st.text_input(
                "Email",
                value=founder.get("email", ""),
                placeholder="Enter email address",
                key=f"email_{founder['id']}"
            )
            founder["role"] = st.selectbox(
                "Role in Startup",
                options=roles,
                index=roles.index(founder.get("role", "CEO")) if founder.get("role") in roles else 0,
                key=f"role_{founder['id']}"
            )


        # Loop through and render forms for all founders
        for founder in st.session_state.founders:
            render_founder_form(founder)


        # Callback function to add a founder
        def add_founder():
            new_id = len(st.session_state.founders) + 1
            st.session_state.founders.append({"id": new_id})


        # Callback function to remove the last founder
        def remove_founder():
            if len(st.session_state.founders) > 1:
                st.session_state.founders.pop()


        # Button to add another founder
        st.button("Add Another Founder", on_click=add_founder)

        # Button to remove the last founder
        if len(st.session_state.founders) > 1:
            st.button("Remove Last Founder", on_click=remove_founder)

        # Final review for submission
        # Fields for this section
        # Section-specific Submit button
        if st.button("Submit Section"):
            # Initialize a list for missing fields in this section
            section_missing_fields = []

            # Validate the fields in this section
            for i, founder in enumerate(st.session_state.get("founders", [])):
                for sub_field in ["first_name", "last_name", "passport_number", "nationality", "role", "email",
                                  "phone_number"]:
                    if not founder.get(sub_field):
                        section_missing_fields.append(f"Founder {i + 1} {sub_field.replace('_', ' ').capitalize()}")

            # Update the missing_fields dictionary
            st.session_state.missing_fields["Founder Details"] = section_missing_fields

            # Provide feedback to the user
            if section_missing_fields:
                st.error("The following fields are missing in this section:\n\n" + "\n".join(
                    f"- {field}" for field in section_missing_fields))
            else:
                st.success("This section's data has been successfully validated!")

    elif selected_section == "Business Profile":
        st.subheader("Business Profile")

        industries = [
            "Select your industry",
            "AI",
            "Agriculture",
            "Biotechnology",
            "Blockchain",
            "Clean Technology",
            "Consulting",
            "Cybersecurity",
            "E-Commerce",
            "Education",
            "Energy",
            "Entertainment",
            "Fintech",
            "Gaming",
            "Healthcare",
            "Hospitality",
            "Manufacturing",
            "Media",
            "Mobility",
            "None",
            "Real Estate",
            "Robotics",
            "SaaS",
            "Telecommunications",
            "Transportation",
            "Wellness",
            "Other"
        ]

        # Ensure the current value of "industry" is valid or fallback to "AI"
        current_industry = st.session_state.get("industry", "Select your industry")
        if current_industry not in industries:
            current_industry = "Select your industry"

        # Industry selection
        st.session_state.industry = st.selectbox(
            "Industry Focus",
            options=industries,
            index=industries.index(current_industry)
        )

        st.session_state.description_prod_serv = st.text_area(
            "Description of Products/Services",
            value=st.session_state.description_prod_serv,
            placeholder="Briefly describe your offerings"
        )

        st.subheader("Revenue Generation:")

        # Revenue inputs
        st.session_state.last_year_revenue = st.text_input(
            "Last Year’s Revenue (EUR)",
            value=st.session_state.get("last_year_revenue", ""),
            placeholder="Enter revenue for the last year"
        )
        st.session_state.current_projected_revenue = st.text_input(
            "Projected Revenue for the End of the Year (EUR)",
            value=st.session_state.get("current_projected_revenue", ""),
            placeholder="Enter projected revenue for the current year"
        )
        st.session_state.next_year_revenue = st.text_input(
            "Projected Revenue for Next Year (EUR)",
            value=st.session_state.get("next_year_revenue", ""),
            placeholder="Enter projected revenue for the next year"
        )

        st.subheader("Funding Information:")
        # Funding information
        st.session_state.amount_raised = st.text_input(
            "Funding Raised (EUR)",
            value=st.session_state.get("amount_raised", ""),
            placeholder="Enter the total funding raised by the startup "
        )

        # Initialize investors in session state
        if "investors" not in st.session_state or not isinstance(st.session_state.investors, list):
            st.session_state.investors = [
                {"id": 1,
                 "type": "Person",
                 "first_name": "",
                 "last_name": "",
                 "passport_id": "",
                 "company_name": "",
                 "registration_number": "",
                 "contact_person": ""
                 }]


        # Callback function to add an investor
        def add_investor():
            new_id = len(st.session_state.investors) + 1
            st.session_state.investors.append(
                {"id": new_id,
                 "type": "Person",
                 "first_name": "",
                 "last_name": "",
                 "passport_id": "",
                 "company_name": "",
                 "registration_number": "",
                 "contact_person": ""
                 })


        # Callback function to remove the last investor
        def remove_investor():
            if len(st.session_state.investors) > 1:  # Ensure at least one investor remains
                st.session_state.investors.pop()


        # Function to render each investor input
        def render_investor_input(investor):
            st.subheader(f"Investor {investor['id']}")

            # Select type of investor
            investor["type"] = st.selectbox(
                f"Type of Investor",
                options=["Person", "Company"],
                index=["Person", "Company"].index(investor.get("type", "Person")),
                key=f"investor_type_{investor['id']}"
            )

            # Fields based on investor type
            if investor["type"] == "Person":
                investor["first_name"] = st.text_input(
                    "First Name",
                    value=investor.get("first_name", ""),
                    placeholder="Enter first name",
                    key=f"first_name_{investor['id']}"
                )
                investor["last_name"] = st.text_input(
                    "Last Name",
                    value=investor.get("last_name", ""),
                    placeholder="Enter last name",
                    key=f"last_name_{investor['id']}"
                )
                investor["passport_id"] = st.text_input(
                    "Passport/ID",
                    value=investor.get("passport_id", ""),
                    placeholder="Enter Passport or ID number",
                    key=f"passport_id_{investor['id']}"
                )
            elif investor["type"] == "Company":
                investor["company_name"] = st.text_input(
                    "Company Name",
                    value=investor.get("company_name", ""),
                    placeholder="Enter company name",
                    key=f"company_name_{investor['id']}"
                )
                investor["registration_number"] = st.text_input(
                    "Registration Number",
                    value=investor.get("registration_number", ""),
                    placeholder="Enter company registration number",
                    key=f"registration_number_{investor['id']}"
                )
                investor["contact_person"] = st.text_input(
                    "Contact Person",
                    value=investor.get("contact_person", ""),
                    placeholder="Enter contact person name",
                    key=f"contact_person_{investor['id']}"
                )


        # Render all investors
        for investor in st.session_state.investors:
            render_investor_input(investor)

        # Add and remove investor buttons
        st.button("Add Another Investor", on_click=add_investor)
        if len(st.session_state.investors) > 1:
            st.button("Remove Last Investor", on_click=remove_investor)

        # Checking before submission
        # Fields for this section
        if st.button("Submit Section"):
            section_missing_fields = []

            # Validate the fields in this section
            for field in section_fields["Business Profile"]:
                if field == "investors":
                    for i, investor in enumerate(st.session_state.get("investors", [])):
                        if investor["type"] == "Person":
                            for sub_field in ["first_name", "last_name", "passport_id"]:
                                if not investor.get(sub_field):
                                    section_missing_fields.append(
                                        f"Investor {i + 1} {sub_field.replace('_', ' ').capitalize()}")
                        elif investor["type"] == "Company":
                            for sub_field in ["company_name", "registration_number", "contact_person"]:
                                if not investor.get(sub_field):
                                    section_missing_fields.append(
                                        f"Investor {i + 1} {sub_field.replace('_', ' ').capitalize()}")
                else:
                    if not st.session_state.get(field) or (
                            field == "industry" and st.session_state[field] == "Select your industry"):
                        section_missing_fields.append(field.replace("_", " ").capitalize())

            # Update the missing fields dictionary
            st.session_state.missing_fields["Business Profile"] = section_missing_fields

            # Provide feedback
            if section_missing_fields:
                st.error("The following fields are missing in this section:\n\n" + "\n".join(
                    f"- {field}" for field in section_missing_fields))
            else:

                st.success("This section's data has been successfully validated!")

    elif selected_section == "Risk and Compliance":
        st.subheader("Risk and Compliance")

        # Initialize session state for Risk and Compliance fields
        if "board_members" not in st.session_state or not isinstance(st.session_state.board_members, list):
            st.session_state.board_members = [{"id": 1, "first_name": "", "last_name": "", "passport_id": ""}]

        if "criminal_record_agreement" not in st.session_state:
            st.session_state["criminal_record_agreement"] = False


        # Callback to add a board member
        def add_board_member():
            new_id = len(st.session_state.board_members) + 1
            st.session_state.board_members.append({"id": new_id, "first_name": "", "last_name": "", "passport_id": ""})


        # Callback to remove the last board member
        def remove_board_member():
            if len(st.session_state.board_members) > 1:
                st.session_state.board_members.pop()


        # Render each board member form and synchronize session state
        def render_board_member_form(member):
            member_id = member["id"]
            first_name = st.text_input(
                f"Board Member {member_id} First Name",
                value=member.get("first_name", ""),
                key=f"first_name_{member_id}"
            )
            last_name = st.text_input(
                f"Board Member {member_id} Last Name",
                value=member.get("last_name", ""),
                key=f"last_name_{member_id}"
            )
            passport_id = st.text_input(
                f"Board Member {member_id} Passport/ID",
                value=member.get("passport_id", ""),
                key=f"passport_id_{member_id}"
            )

            # Update session state with current form values
            member["first_name"] = first_name
            member["last_name"] = last_name
            member["passport_id"] = passport_id


        # Render forms for all board members
        for member in st.session_state.board_members:
            render_board_member_form(member)

        # Add and Remove buttons for board members
        st.button("Add Board Member", on_click=add_board_member)
        if len(st.session_state.board_members) > 1:
            st.button("Remove Last Board Member", on_click=remove_board_member)

        # Criminal Record Declaration
        st.subheader("Criminal Record Declaration")
        declaration_text = (
            f"I hereby declare, to the best of my knowledge and belief, "
            f"that I and any board members associated with the startup '{st.session_state.startup_name}' "
            f"have no criminal records or pending investigations in any jurisdiction.\n"
            f"This declaration is made in good faith."
        )
        st.text_area("Declaration", value=declaration_text, height=100, disabled=True)

        # Checkbox for Agreement
        st.session_state["criminal_record_agreement"] = st.checkbox(
            "I agree to the above declaration and confirm that it is accurate.",
            value=st.session_state["criminal_record_agreement"],
            key="criminal_record_agreement_checkbox"
        )

        # Submit Section Button
        if st.button("Submit Section"):
            section_missing_fields = []

            # Validate board members
            for i, member in enumerate(st.session_state.board_members):
                if not member.get("first_name"):
                    section_missing_fields.append(f"Board Member {i + 1} First Name")
                if not member.get("last_name"):
                    section_missing_fields.append(f"Board Member {i + 1} Last Name")
                if not member.get("passport_id"):
                    section_missing_fields.append(f"Board Member {i + 1} Passport/ID")

            # Validate criminal record agreement
            if not st.session_state["criminal_record_agreement"]:
                section_missing_fields.append("Criminal record agreement")

            # Provide feedback
            if section_missing_fields:
                st.error(
                    "The following fields are missing in this section:\n\n" +
                    "\n".join(f"- {field}" for field in section_missing_fields))
            else:
                st.success("This section's data has been successfully validated!")

    elif selected_section == "Sustainability and Social Impact":
        st.subheader("Sustainability and Social Impact")

        # Define options for each field
        sustainability_goals_options = [
            "None",
            "Carbon Reduction",
            "Waste Management",
            "Energy Efficiency",
            "Water Conservation",
            "Renewable Energy Adoption",
            "Circular Economy",
            "Biodiversity Preservation",
            "Sustainable Sourcing",
            "Plastic Reduction"
        ]

        environmental_impact_options = [
            "None",
            "Reduce Greenhouse Gas Emissions",
            "Minimize Waste Production",
            "Enhance Recycling",
            "Switch to Renewable Energy",
            "Reduce Water Usage",
            "Implement Energy-Efficient Practices",
            "Adopt Green Building Standards",
            "Promote Sustainable Transportation",
            "Use Biodegradable Materials",
            "Protect Ecosystems and Wildlife"
        ]

        social_contribution_options = [
            "None",
            "Promote Diversity in Hiring",
            "Ensure Pay Equity",
            "Foster Inclusive Workplace Culture",
            "Support Community Programs",
            "Provide Scholarships",
            "Encourage Employee Volunteering",
            "Engage with Underrepresented Groups",
            "Provide Accessible Products/Services",
            "Collaborate with Social Enterprises",
            "Advocate for Human Rights"
        ]

        # Ensure session state is initialized with valid default values
        if "sustainability_goals" not in st.session_state or st.session_state[
            "sustainability_goals"] not in sustainability_goals_options:
            st.session_state["sustainability_goals"] = "None"
        if "environment_impact_description" not in st.session_state or st.session_state[
            "environment_impact_description"] not in environmental_impact_options:
            st.session_state["environment_impact_description"] = "None"
        if "social_impact_contributions" not in st.session_state or st.session_state[
            "social_impact_contributions"] not in social_contribution_options:
            st.session_state["social_impact_contributions"] = "None"

        # Sustainability Goals
        sustainability_goal = st.selectbox(
            "Sustainability Goal",
            options=sustainability_goals_options,
            index=sustainability_goals_options.index(st.session_state["sustainability_goals"]) if st.session_state[
                                                                                                      "sustainability_goals"] in sustainability_goals_options else 0,
            key="sustainability_goals_select",
        )
        st.session_state["sustainability_goals"] = sustainability_goal

        # Environmental Impact
        environmental_impact = st.selectbox(
            "Environmental Impact",
            options=environmental_impact_options,
            index=environmental_impact_options.index(st.session_state["environment_impact_description"]) if
            st.session_state["environment_impact_description"] in environmental_impact_options else 0,
            key="environment_impact_select",
        )
        st.session_state["environment_impact_description"] = environmental_impact

        # Social Contributions
        social_contribution = st.selectbox(
            "Social Contribution",
            options=social_contribution_options,
            index=social_contribution_options.index(st.session_state["social_impact_contributions"]) if
            st.session_state["social_impact_contributions"] in social_contribution_options else 0,
            key="social_contributions_select",
        )
        st.session_state["social_impact_contributions"] = social_contribution

        # Final Check
        if st.button("Submit Section"):
            section_missing_fields = []

            # Validate the fields in this section
            if st.session_state["sustainability_goals"] == "None":
                section_missing_fields.append("Sustainability Goal")
            if st.session_state["environment_impact_description"] == "None":
                section_missing_fields.append("Environmental Impact")
            if st.session_state["social_impact_contributions"] == "None":
                section_missing_fields.append("Social Contribution")

            # Provide feedback
            if section_missing_fields:
                st.error(
                    "The following fields are missing or incomplete:\n\n"
                    + "\n".join(f"- {field}" for field in section_missing_fields))
            else:
                st.success("This section's data has been successfully validated!")

    elif selected_section == "Additional Documents":
        st.subheader("Additional Documents")

        # Proof of Incorporation
        st.file_uploader(
            "Proof of Incorporation: Provide an official registration document for your startup.",
            type=["pdf"],
            key="incorporation_proof"
        )

        # Financial Statements
        st.file_uploader(
            "Financial Statements: Provide your financial statements for the last two years.",
            type=["pdf"],
            key="financial_statements"
        )

        # Environmental Certifications
        st.file_uploader(
            "Certifications: Provide a certification proving sustainable practices.",
            type=["pdf"],
            key="environmental_certifications"
        )

        # Final Check
        # Submit button and Saves in CSV

        # Submit button for all checks
        if st.button("Submit All"):
            # Collect missing fields from all sections
            all_missing_fields = []
            for section, fields in st.session_state.missing_fields.items():
                if fields:
                    all_missing_fields.append(f"**{section}:**")
                    all_missing_fields.extend(f"- {field}" for field in fields)

            if all_missing_fields:
                # Display missing fields across all sections
                st.error("Some fields are still missing:\n\n" + "\n".join(all_missing_fields))
            else:
                # Save all data to CSV
                data = {key: st.session_state[key] for key in st.session_state if
                        key not in ["selected_section", "logged_in", "missing_fields"]}
                df = pd.DataFrame([data])
                df.to_csv("submission_data.csv", index=False)
                db.add_to_startups(st.session_state)
                db.add_to_founders_details(st.session_state)
                db.add_to_startup_profile(st.session_state)
                db.add_to_investors(st.session_state)
                db.add_to_board_members(st.session_state)
                db.add_to_sustainability(st.session_state)
                db.close_connection()
                st.success("All sections are complete! Your data has been successfully submitted and saved!")

