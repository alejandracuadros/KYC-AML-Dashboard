import streamlit as st
import pandas as pd
import plotly.express as px
from db_utils import _connect_to_db, close_db_connection
from st_aggrid import AgGrid
import numpy as np

# Set up Streamlit page
st.set_page_config(page_title="Executive Dashboard", layout="wide")
st.markdown(
    """
    <style>
    .stAppHeader {
        background-color: #05254F; /
        font-family: 'Arial', sans-serif;
    }

    .stApp {
        background-color: #05254F; 
        font-family: 'Arial', sans-serif;  
        color: #003366; 
    }
        
    .stSidebar { 
        background-color: #05254F; 
        color: white ; 
        font-family: 'Arial', sans-serif;
    }
    button {
            background-color: #073470 !important;
            color: white !important;
            font-family: 'Arial', sans-serif; 
        }
    button:hover {
        background-color: #135F91 !important; 
    }
    /* Titles and subtitles */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF; /* Light blue */
        font-family: 'Arial', sans-serif;
    }

    /* Customize metric containers */
    .metric-container {
        background-color: #05254F; /* Light gray for contrast */
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        height: 120px;
        padding: 10px;
        display: flex;
        border-radius: 10px;
        margin-bottom: 15px;
        border: 0.5px solid #7F7F7F; 
        
    }
    .metric-title {
        color: #FFFFFF; /* Dark blue */
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 3px;
    }
    .metric-value {
        font-size: 40px;
        font-weight: bold;
        color: #FFFFFF; /* Light blue */;
    }
    .visual-container {
    background-color: #05254F; /* Morgan Stanley dark blue */
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    border: 0.5px solid #FFFFFF; /* White border for contrast */
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}
    .visual-title {
    color: #FFFFFF; /* White text for titles */
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

     /* Scrollbar customization */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background: #0071CE; /* Light blue */
        border-radius: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #003366; /* Dark blue */
    }

    /* Table customization */
    .dataframe {
        border: 2px solid #0071CE; /* Table border matches branding */
        border-radius: 10px;
        overflow: hidden;
    }

    /* Interactive elements like buttons */
    .stButton button {
        background-color: #003366; /* Dark blue */
        color: #FFFFFF; /* White text */
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        border: none;
    }
    .stButton button:hover {
        background-color: #0071CE; /* Light blue on hover */
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Fetch data utility
def fetch_data(query):
    connection = _connect_to_db("regulatory_compliance")
    try:
        data = pd.read_sql(query, connection)
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()
    finally:
        close_db_connection(connection)

# Fetch required data
startups_query = "SELECT * FROM startups;"
profiles_query = "SELECT * FROM startup_profile;"
startups_data = fetch_data(startups_query)
profiles_data = fetch_data(profiles_query)


# Sidebar menu using buttons
st.sidebar.title("Choose Dashboard View:")
if "menu_option" not in st.session_state:
    st.session_state.menu_option = "All Startups"  # Default view

if st.sidebar.button("All Startups"):
    st.session_state.menu_option = "All Startups"

if st.sidebar.button("Startup-Specific Insights"):
    st.session_state.menu_option = "Startup-Specific Insights"

menu_option = st.session_state.menu_option

st.header(" Automated KYC / AML Startup Reports")

if menu_option == "All Startups":
    st.header("All Startups")
    if not startups_data.empty and not profiles_data.empty:
        merged_data = startups_data.merge(profiles_data, on="startup_id", how="left")

        # Layout: Centered Summary Metrics
        # st.subheader(" ")

        # Create columns for metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Total Startups</div>"
                f"<div class='metric-value'>{startups_data.shape[0]}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col2:
            num_industries = profiles_data["industry"].nunique()
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Number of Industries</div>"
                f"<div class='metric-value'>{num_industries}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col3:
            avg_projected_revenue = profiles_data["current_projected_revenue"].mean()
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Avg Projected Revenue</div>"
                f"<div class='metric-value'>${avg_projected_revenue:,.0f}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col4:
            total_fundraising = profiles_data["amount_raised"].sum()
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Total Fundraising</div>"
                f"<div class='metric-value'>${total_fundraising:,.0f}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        # Row 1: Geographical Hotspots, Average Fundraising, Revenue Distribution
        st.markdown(" ")
        row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

        with row1_col1:
            fundraising_by_geo = merged_data.groupby("country")["amount_raised"].sum().reset_index()
            fig1 = px.choropleth(
                fundraising_by_geo,
                locations="country",
                locationmode="country names",
                color="amount_raised",
                title="Geographical Hotspots for Fundraising",
                labels={"amount_raised": "Total Raised ($)"},
                color_continuous_scale=px.colors.sequential.Plasma,
            )
            # Set background color, adjust map scale, and position the color scale horizontally
            fig1.update_layout(
                paper_bgcolor="#05254F",  # Background outside the chart area
                plot_bgcolor="#05254F",  # Background inside the chart area
                geo=dict(
                    projection_scale=1.3,  # Increase the scale of the map (default is 1)
                    center={"lat": 10, "lon": 0},  # Adjust center if needed (optional)
                    visible=True,  # Ensure the map is visible
                ),
                coloraxis_colorbar=dict(
                    orientation="h",  # Horizontal orientation
                    x=0.5,  # Center the color scale horizontally
                    xanchor="center",
                    y=-0.2,  # Position below the chart
                    len=1.13,  # Adjust length of the color bar
                    title=dict(
                        text="Total Raised ($)",  # Title text
                        font=dict(size=12),  # Font size for the title
                    ),
                    tickfont=dict(size=10),  # Font size for the ticks
                )
            )
            st.plotly_chart(fig1, use_container_width=True)

        with row1_col2:
            fundraising_by_industry = profiles_data.groupby("industry")["amount_raised"].mean().reset_index()
            fig2 = px.bar(
                fundraising_by_industry,
                x="industry",
                y="amount_raised",
                title="Average Fundraising by Industry",
                labels={"industry": "Industry", "amount_raised": "Avg Raised ($)"},
                color="industry",
            )

            fig2.update_layout(
                paper_bgcolor="#05254F",  # Background outside the chart area
                plot_bgcolor="#05254F",  # Background inside the chart area
                showlegend=False  # Hide the legend
            )

            st.plotly_chart(fig2, use_container_width=True)

        with row1_col3:
            fig3 = px.violin(
                profiles_data,
                x="industry",
                y="last_year_revenue",
                color="industry",
                box=True,
                points="all",
                title="Revenue Distribution Across Industries",
                labels={"industry": "Industry", "last_year_revenue": "Revenue ($)"},
            )
            fig3.update_layout(
                paper_bgcolor="#05254F",
                plot_bgcolor="#05254F",
                showlegend=False  # Hide the legend
            )
            st.plotly_chart(fig3, use_container_width=True)

        # Fundraising Activity by Year
        merged_data["year_of_incorporation"] = pd.to_datetime(merged_data["date_of_incorporation"]).dt.year
        fundraising_by_year = merged_data.groupby("year_of_incorporation")["amount_raised"].sum().reset_index()
        fundraising_by_year["trendline"] = np.poly1d(
            np.polyfit(fundraising_by_year["year_of_incorporation"], fundraising_by_year["amount_raised"], 1)
        )(fundraising_by_year["year_of_incorporation"])

        with row1_col4:
            fig4 = px.line(
                fundraising_by_year,
                x="year_of_incorporation",
                y="amount_raised",
                title="Fundraising Activity by Year",
                markers=True,
                labels={
                    "year_of_incorporation": "Year of Incorporation",  # Custom X-axis label
                    "amount_raised": "Total Amount Raised ($)"  # Custom Y-axis label
                }
            )
            fig4.add_scatter(
                x=fundraising_by_year["year_of_incorporation"],
                y=fundraising_by_year["trendline"],
                mode="lines",
                name="Trendline",
                line=dict(color="red", dash="dash"),
            )
            fig4.update_layout(
                paper_bgcolor="#05254F",  # Background outside the chart area
                plot_bgcolor="#05254F",  # Background inside the chart area
                legend=dict(
                    orientation="h",  # Horizontal legend
                    x=0.5,  # Center horizontally
                    xanchor="right",
                    y=1,  # Position at the top inside the chart
                    yanchor="top",  # Align with the top of the chart
                    font=dict(size=8)  # Adjust legend font size
                ),

            )
            st.plotly_chart(fig4, use_container_width=True)

        # Row 2: Fundraising Activity, Startups by Country, Average Employees
        row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

        with row2_col1:
            country_counts = startups_data["country"].value_counts().reset_index()
            country_counts.columns = ["Country", "Startup Count"]
            fig5 = px.treemap(
                country_counts,
                path=["Country"],
                values="Startup Count",
                title="Startups by Country",
            )
            fig5.update_layout(
                paper_bgcolor="#05254F",
                plot_bgcolor="#05254F"
            )
            st.plotly_chart(fig5, use_container_width=True)


        profiles_cleaned = profiles_data.merge(
            startups_data[["startup_id", "country"]],
            on="startup_id",
            how="left"
        ).dropna(subset=["last_year_revenue", "current_projected_revenue"])

        with row2_col2:
            fig7 = px.scatter(
                profiles_cleaned,
                x="last_year_revenue",
                y="current_projected_revenue",
                size="amount_raised",
                color="country",
                title="Last Year vs Projected Revenue",
                labels={
                    "last_year_revenue": "Last Year's Revenue ($)",  # Custom X-axis label
                    "current_projected_revenue": "Projected Revenue ($)",  # Custom Y-axis label
                    "amount_raised": "Amount Raised ($)",  # Optional: Legend label for size
                    "country": "Country"  # Optional: Legend label for color
                }
            )
            fig7.update_layout(
                paper_bgcolor="#05254F",
                plot_bgcolor="#05254F",
                showlegend = False
            )
            st.plotly_chart(fig7, use_container_width=True)

        with row2_col3:
            top_startups = profiles_data.nlargest(10, "current_projected_revenue")[
                ["startup_id", "current_projected_revenue"]]
            top_startups = top_startups.merge(startups_data[["startup_id", "startup_name"]], on="startup_id")
            fig8 = px.bar(
                top_startups,
                x="current_projected_revenue",
                y="startup_name",
                orientation="h",
                title="Top 10 Startups by Projected Revenue",
                labels={
                    "current_projected_revenue": "Projected Revenue ($)",  # Custom X-axis label
                    "startup_name": "Startup Name"  # Custom Y-axis label
                }
            )
            fig8.update_layout(
                paper_bgcolor="#05254F",
                plot_bgcolor="#05254F",
                showlegend=False  # Hides legend
            )
            st.plotly_chart(fig8, use_container_width=True)

        with row2_col4:
            # Calculate trendline manually using numpy
            profiles_cleaned["trendline"] = np.poly1d(
                np.polyfit(profiles_cleaned["amount_raised"], profiles_cleaned["last_year_revenue"], 1)
            )(profiles_cleaned["amount_raised"])

            # Create scatter plot
            fig9 = px.scatter(
                profiles_cleaned,
                x="amount_raised",
                y="last_year_revenue",
                title="Fundraising Efficiency: Amount Raised vs Revenue",
                labels={"amount_raised": "Amount Raised ($)", "last_year_revenue": "Revenue ($)"},
                color="industry",
            )

            # Add trendline
            fig9.add_scatter(
                x=profiles_cleaned["amount_raised"],
                y=profiles_cleaned["trendline"],
                mode="lines",
                name="Trendline",
                line=dict(color="red", dash="dash"),
            )

            fig9.update_layout(
                paper_bgcolor="#05254F",
                plot_bgcolor="#05254F",
                showlegend = False
            )
            st.plotly_chart(fig9, use_container_width=True)

        # Interactive Data Table
        st.markdown("### Detailed Data")
        AgGrid(merged_data, height=300, fit_columns_on_grid_load=True)

elif menu_option == "Startup-Specific Insights":
    st.header("Startup-Specific Insights")
    if not startups_data.empty and not profiles_data.empty:
        merged_data = startups_data.merge(profiles_data, on="startup_id", how="left")

        # Dropdown to select a startup
        startup_names = startups_data["startup_name"].unique()
        selected_startup = st.selectbox("Select a Startup:", startup_names)

        # Filter data for the selected startup
        filtered_data = merged_data[merged_data["startup_name"] == selected_startup]

        # Metrics for Startup-Specific Insights
        col1, col2, col3 = st.columns(3)

        # Existing KPIs
        with col1:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Industry</div>"
                f"<div class='metric-value'>{filtered_data['industry'].iloc[0]}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Projected Revenue</div>"
                f"<div class='metric-value'>${filtered_data['current_projected_revenue'].sum():,.0f}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col3:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Total Amount Raised</div>"
                f"<div class='metric-value'>${filtered_data['amount_raised'].sum():,.0f}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        # Additional KPIs
        col4, col5, col6 = st.columns(3)

        company_size_cleaned = filtered_data["company_size"].iloc[0].split("(")[0].strip()

        with col4:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Company Size</div>"
                f"<div class='metric-value' style='font-size: 33px;'>{company_size_cleaned}</div>"
        "</div>",
                unsafe_allow_html=True,
            )

        with col5:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Number of Employees</div>"
                f"<div class='metric-value'>{filtered_data['employees'].iloc[0]}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col6:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Last Year's Revenue</div>"
                f"<div class='metric-value'>${filtered_data['last_year_revenue'].sum():,.0f}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        col7, col8, col9 = st.columns(3)

        with col7:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Next Year's Projected Revenue</div>"
                f"<div class='metric-value'>${filtered_data['next_year_revenue'].sum():,.0f}</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col8:
            revenue_growth = (
                ((filtered_data['next_year_revenue'].sum() - filtered_data['last_year_revenue'].sum()) /
                 filtered_data['last_year_revenue'].sum()) * 100
                if filtered_data['last_year_revenue'].sum() > 0 else 0
            )
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Revenue Growth Potential</div>"
                f"<div class='metric-value'>{revenue_growth:.2f}%</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        with col9:
            st.markdown(
                "<div class='metric-container'>"
                "<div class='metric-title'>Country of Origin</div>"
                f"<div class='metric-value'>{filtered_data['country'].iloc[0]}</div>"
                "</div>",
                unsafe_allow_html=True,
            )




