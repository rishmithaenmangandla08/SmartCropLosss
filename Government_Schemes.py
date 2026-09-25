import streamlit as st


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Government Schemes",
    page_icon="🏛️",
    layout="wide"
)


# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🏛️ Government Schemes for Farmers")

st.markdown("""
### 🌾 Government Support & Scheme Information

This page helps farmers discover major agriculture-related
Government of India schemes and access their official portals.

Use the information below as a starting point and verify
current eligibility, application dates and state-specific
conditions on the official government website before applying.
""")


st.divider()


# ==========================================================
# FARMER DETAILS
# ==========================================================

st.header("👨‍🌾 Farmer Information")

col1, col2 = st.columns(2)

with col1:

    farmer_name = st.text_input(
        "Farmer Name",
        key="scheme_farmer_name"
    )

    state = st.selectbox(
        "State",
        [
            "Telangana",
            "Andhra Pradesh",
            "Karnataka",
            "Tamil Nadu",
            "Maharashtra",
            "Karnataka",
            "Kerala",
            "Odisha",
            "West Bengal",
            "Madhya Pradesh",
            "Uttar Pradesh",
            "Rajasthan",
            "Gujarat",
            "Punjab",
            "Haryana",
            "Bihar",
            "Jharkhand",
            "Chhattisgarh",
            "Assam",
            "Other"
        ],
        key="scheme_state"
    )


with col2:

    district = st.text_input(
        "District",
        key="scheme_district"
    )

    land_holding = st.number_input(
        "Land Holding (Acres)",
        min_value=0.0,
        value=1.0,
        step=0.5,
        key="scheme_land"
    )


st.divider()


# ==========================================================
# SCHEME DATABASE
# ==========================================================

schemes = {

    "PM-KISAN Samman Nidhi": {
        "icon": "💰",
        "category": "Income Support",
        "description": (
            "Provides income support to eligible landholding "
            "farmer families under the PM-KISAN scheme."
        ),
        "benefit": (
            "The official PM-KISAN portal currently states "
            "income support of ₹6,000 per year in three equal "
            "installments, subject to the scheme's eligibility "
            "and exclusion criteria."
        ),
        "eligibility": (
            "Eligibility is determined under the PM-KISAN "
            "guidelines. Landholding status and exclusion "
            "criteria apply."
        ),
        "action": "Check Status / New Farmer Registration",
        "url": "https://pmkisan.gov.in/"
    },


    "Pradhan Mantri Fasal Bima Yojana": {
        "icon": "🛡️",
        "category": "Crop Insurance",
        "description": (
            "Agricultural crop insurance support for notified "
            "crops and areas under the applicable scheme rules."
        ),
        "benefit": (
            "Provides crop-insurance related services including "
            "application, premium calculation, policy status and "
            "crop-loss grievance support."
        ),
        "eligibility": (
            "Eligibility, notified crops, areas and applicable "
            "conditions depend on the relevant season and scheme "
            "notifications."
        ),
        "action": "Apply / Check Insurance Information",
        "url": "https://pmfby.gov.in/"
    },


    "Kisan Credit Card (KCC)": {
        "icon": "💳",
        "category": "Agricultural Credit",
        "description": (
            "Provides timely credit support for agricultural "
            "operations and certain allied activities."
        ),
        "benefit": (
            "The myScheme portal describes KCC as a credit facility "
            "for cultivation, post-harvest expenses, marketing loans, "
            "working capital and eligible agricultural/allied needs."
        ),
        "eligibility": (
            "The myScheme listing includes owner cultivators, "
            "tenant farmers, sharecroppers, oral lessees and eligible "
            "SHGs/JLGs, subject to applicable bank and scheme rules."
        ),
        "action": "Check Eligibility / Apply",
        "url": "https://www.myscheme.gov.in/schemes/kcc"
    },


    "Soil Health Card": {
        "icon": "🧪",
        "category": "Soil Management",
        "description": (
            "Provides information about soil nutrient status and "
            "supports fertilizer and soil-amendment recommendations."
        ),
        "benefit": (
            "The Soil Health Card framework covers soil parameters "
            "and provides advisory information on fertilizers and "
            "soil amendments."
        ),
        "eligibility": (
            "Farmers can use the Soil Health Card system to obtain "
            "soil-related information and recommendations."
        ),
        "action": "Access Soil Health Services",
        "url": "https://soilhealth.dac.gov.in/"
    },


    "Pradhan Mantri Krishi Sinchayee Yojana": {
        "icon": "💧",
        "category": "Irrigation & Water Management",
        "description": (
            "Supports irrigation development and more efficient "
            "use of agricultural water resources."
        ),
        "benefit": (
            "The PMKSY guidelines emphasize improved access to "
            "irrigation and better on-farm water-use efficiency."
        ),
        "eligibility": (
            "Implementation and assistance can depend on the "
            "specific component, state and applicable guidelines."
        ),
        "action": "Learn About Irrigation Support",
        "url": "https://pmksy.gov.in/"
    }
}


# ==========================================================
# SEARCH / FILTER
# ==========================================================

st.header("🔎 Find a Government Scheme")

search_term = st.text_input(
    "Search Scheme",
    placeholder="Example: crop insurance, loan, soil, irrigation",
    key="scheme_search"
)


selected_category = st.selectbox(
    "Filter by Category",
    [
        "All",
        "Income Support",
        "Crop Insurance",
        "Agricultural Credit",
        "Soil Management",
        "Irrigation & Water Management"
    ],
    key="scheme_category"
)


# ==========================================================
# FILTER SCHEMES
# ==========================================================

filtered_schemes = {}

for scheme_name, scheme_info in schemes.items():

    matches_search = True

    if search_term.strip():

        text_to_search = (
            scheme_name
            + " "
            + scheme_info["description"]
            + " "
            + scheme_info["category"]
        ).lower()

        matches_search = (
            search_term.lower().strip()
            in text_to_search
        )


    matches_category = (
        selected_category == "All"
        or scheme_info["category"] == selected_category
    )


    if matches_search and matches_category:

        filtered_schemes[scheme_name] = scheme_info


# ==========================================================
# DISPLAY SCHEMES
# ==========================================================

st.divider()

st.header("📋 Available Schemes")


if not filtered_schemes:

    st.warning(
        "No schemes matched your search."
    )


for scheme_name, scheme_info in filtered_schemes.items():

    with st.expander(
        f"{scheme_info['icon']} {scheme_name}"
    ):

        st.write(
            f"**Category:** {scheme_info['category']}"
        )

        st.write(
            f"**About:** {scheme_info['description']}"
        )

        st.write(
            f"**Support / Benefit:** {scheme_info['benefit']}"
        )

        st.write(
            f"**Eligibility:** {scheme_info['eligibility']}"
        )

        st.write(
            f"**Recommended Action:** {scheme_info['action']}"
        )

        st.link_button(
            "🌐 Open Official Website",
            scheme_info["url"]
        )


# ==========================================================
# SIMPLE FARMER RELEVANCE ASSISTANT
# ==========================================================

st.divider()

st.header("🤖 Scheme Relevance Assistant")

st.write(
    "Select your current farming requirement to see "
    "which scheme categories may be relevant."
)


requirement = st.selectbox(
    "What type of support are you looking for?",
    [
        "Income Support",
        "Crop Insurance",
        "Agricultural Loan / Credit",
        "Soil Testing / Fertilizer Advice",
        "Irrigation / Water Management"
    ],
    key="scheme_requirement"
)


if st.button(
    "🔍 Find Relevant Scheme",
    key="find_relevant_scheme"
):

    if requirement == "Income Support":

        st.success(
            "PM-KISAN Samman Nidhi is the relevant category "
            "to review. Check the official PM-KISAN portal "
            "for current eligibility and status."
        )

        st.link_button(
            "Open PM-KISAN",
            "https://pmkisan.gov.in/"
        )


    elif requirement == "Crop Insurance":

        st.success(
            "Pradhan Mantri Fasal Bima Yojana (PMFBY) is the "
            "relevant crop-insurance scheme to review."
        )

        st.link_button(
            "Open PMFBY",
            "https://pmfby.gov.in/"
        )


    elif requirement == "Agricultural Loan / Credit":

        st.success(
            "Kisan Credit Card (KCC) is the relevant credit "
            "scheme to review."
        )

        st.link_button(
            "Open KCC Information",
            "https://www.myscheme.gov.in/schemes/kcc"
        )


    elif requirement == "Soil Testing / Fertilizer Advice":

        st.success(
            "The Soil Health Card system is relevant for "
            "soil nutrient information and fertilizer/soil "
            "amendment advice."
        )

        st.link_button(
            "Open Soil Health Card",
            "https://soilhealth.dac.gov.in/"
        )


    elif requirement == "Irrigation / Water Management":

        st.success(
            "Pradhan Mantri Krishi Sinchayee Yojana (PMKSY) "
            "is the relevant irrigation and water-management "
            "programme to review."
        )

        st.link_button(
            "Open PMKSY",
            "https://pmksy.gov.in/"
        )


# ==========================================================
# IMPORTANT INFORMATION
# ==========================================================

st.divider()

st.subheader("⚠️ Important")

st.info("""
Government schemes can have specific eligibility conditions,
state-level implementation rules, application windows and
document requirements.

Always verify the latest information on the official government
portal before submitting an application.
""")


# ==========================================================
# SOURCES
# ==========================================================

st.subheader("🌐 Official Portals")

st.link_button(
    "PM-KISAN",
    "https://pmkisan.gov.in/"
)

st.link_button(
    "PMFBY",
    "https://pmfby.gov.in/"
)

st.link_button(
    "myScheme",
    "https://www.myscheme.gov.in/"
)

st.link_button(
    "Soil Health Card",
    "https://soilhealth.dac.gov.in/"
)

st.link_button(
    "PMKSY",
    "https://pmksy.gov.in/"
)


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🏛️ Government Scheme Information | "
    "Verify current eligibility and scheme conditions "
    "with the relevant official government portal."
)