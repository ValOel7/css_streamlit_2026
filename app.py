import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Academic CV Portfolio",
    layout="wide",
)

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def section_header(title: str, subtitle: str | None = None) -> None:
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.divider()

def experience_item(role: str, org_line: str, dates_location: str, bullets: list[str]) -> None:
    with st.container(border=True):
        st.subheader(role)
        st.caption(org_line)
        st.caption(dates_location)
        st.markdown("**Key responsibilities / achievements:**")
        for b in bullets:
            st.write(f"• {b}")

def qualification_item(qualification: str, field: str, institution: str, dates: str) -> None:
    with st.container(border=True):
        st.subheader(qualification)
        st.caption(field)
        st.caption(institution)
        st.caption(dates)

# -------------------------------------------------
# Sidebar Profile Navigation
# -------------------------------------------------
st.sidebar.title("Profile Navigation")
menu = st.sidebar.radio(
    "Select section",
    ["Academic Profile", "Experience", "Qualifications", "Contact"],
)

st.sidebar.divider()
st.sidebar.caption("Academic CV portfolio")

# =================================================
# Academic Profile
# =================================================
if menu == "Academic Profile":
    section_header("Valusha Oelofse Academic Profile")

    col1, col2 = st.columns([1, 3], gap="large")

    with col1:
        st.image(
            "https://media.licdn.com/dms/image/v2/D4D03AQEep1ngJFGRvw/profile-displayphoto-scale_400_400/B4DZvu5VAOGUAg-/0/1769239565802?e=1771459200&v=beta&t=LseAPd591Le3-pb-BhzUUnn5oUvsFkWG_LQZ-UuFXD8",
            width=170,
        )

    with col2:
        with st.container(border=True):
            st.subheader("Junior Lecturer and Aspiring Data Scientist")
            st.caption("Department of Economics and Finance")
            st.caption("University of the Free State")

        st.markdown("### Profile Summary")
        st.write(
            "My passion lies in leveraging data to solve complex financial and "
            "business challenges. My experiences encompass data analytics, "
            "dashboard creation, data preprocessing, and developing machine learning models. "
            "My research focuses on designing a Social Stress Indicator which has sharpened "
            "my analytical and problem-solving expertise."
        )

# =================================================
# Experience
# =================================================
elif menu == "Experience":
    section_header("Experience")

    experience_item(
        role="Junior Lecturer",
        org_line="University of the Free State · Contract",
        dates_location="February 2025 – Present · Bloemfontein, Free State, South Africa (On-site)",
        bullets=[
            "Lecturing and supporting undergraduate modules in quantitative and data-oriented subjects",
            "Designing and delivering tutorials and practical sessions",
            "Assessment, marking, and academic moderation",
            "Supporting student development in data analysis and problem-solving skills",
        ],
    )

    experience_item(
        role="Data Analyst",
        org_line="Interdisciplinary Centre for Digital Futures (ICDF), University of the Free State · Contract",
        dates_location="July 2023 – December 2024 · Bloemfontein, Free State, South Africa (On-site)",
        bullets=[
            "Conducted data analysis in support of interdisciplinary research initiatives",
            "Performed data cleaning, exploratory analysis, and modelling",
            "Produced analytical outputs and visualisations for research and reporting purposes",
            "Collaborated with academic and research stakeholders across disciplines",
        ],
    )

    experience_item(
        role="Intern",
        org_line="Quantify Your Future · Virtual Internship (Powered by SAGEA)",
        dates_location="January 2023 – February 2023 · Remote",
        bullets=[
            "Participated in industry-aligned data analytics projects with FirstRand, Absa, and Nedbank",
            "Gained practical exposure to data framing, exploration, modelling, and visualisation",
            "Developed core professional skills including critical thinking, collaboration, and communication",
            "Completed team-based projects facilitated by financial industry partners",
        ],
    )

    experience_item(
        role="Demonstrator",
        org_line="University of the Free State · Contract",
        dates_location="September 2022 – November 2022 · Bloemfontein, South Africa",
        bullets=[
            "Assisted students during practical sessions for module CSIS1644",
            "Provided academic support and clarification of module content",
            "Invigilated tests and supported assessment processes",
        ],
    )

    experience_item(
        role="Demonstrator",
        org_line="University of the Free State · Contract",
        dates_location="February 2022 – July 2022 · Bloemfontein, Free State, South Africa",
        bullets=[
            "Supported practical sessions for module CSIS1614",
            "Answered student queries related to course content and assessments",
            "Assisted with invigilation and administrative academic duties",
        ],
    )

# =================================================
# Qualifications
# =================================================
elif menu == "Qualifications":
    section_header("Qualifications")

    qualification_item(
        qualification="Master of Commerce (MCom)",
        field="Business and Financial Analytics",
        institution="University of the Free State",
        dates="January 2025 – December 2025",
    )

    qualification_item(
        qualification="Bachelor of Commerce Honours (BCom Hons)",
        field="Business and Financial Analytics",
        institution="University of the Free State",
        dates="January 2024 – December 2024",
    )

    qualification_item(
        qualification="Bachelor of Commerce (BCom)",
        field="Business and Financial Analytics",
        institution="University of the Free State",
        dates="2021 – 2023",
    )

# =================================================
# Contact
# =================================================
elif menu == "Contact":
    section_header("Contact")

    with st.container(border=True):
        st.subheader("Get in touch")

        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown("**Email:**")
            st.write("valusha.oel@gmail.com")  # add email here

        with col2:
            st.markdown("**Institution:**")
            st.write("University of the Free State")  # update as needed

        st.divider()

        # Streamlit-native link button (works on newer Streamlit versions)
        try:
            st.link_button("View LinkedIn Profile", "https://www.linkedin.com/in/valentinaoelofse/")
        except Exception:
            # Fallback for older versions
            st.markdown("[View LinkedIn Profile](https://www.linkedin.com/in/valentinaoelofse/)")
