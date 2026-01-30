import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Academic CV Portfolio",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS (Professional Purple Theme)
# -------------------------------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #f7f5fb;
    }
    .main {
        background-color: #f7f5fb;
    }
    h1, h2, h3 {
        color: #4b2e83;
    }
    .stSidebar {
        background-color: #ede9f5;
    }
    .cv-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 6px;
        border-left: 5px solid #4b2e83;
        margin-bottom: 1rem;
    }
    .section-title {
        border-bottom: 1px solid #d6cfee;
        padding-bottom: 0.3rem;
        margin-bottom: 0.8rem;
    }
    .small-text {
        font-size: 0.9rem;
        color: #555555;
    }
    .linkedin-button {
        background-color: #4b2e83;
        color: white !important;
        padding: 0.45rem 0.9rem;
        text-decoration: none;
        border-radius: 4px;
        font-weight: 500;
    }
    .linkedin-button:hover {
        background-color: #3b2366;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Sidebar Profile Navigation
# -------------------------------------------------
st.sidebar.title("Profile Navigation")
menu = st.sidebar.radio(
    "Select section",
    [
        "Academic Profile",
        "Experience",
        "Qualifications",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Academic CV portfolio")

# =================================================
# Academic Profile
# =================================================
if menu == "Academic Profile":
    st.title("Academic Profile")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "https://media.licdn.com/dms/image/v2/D4D03AQEep1ngJFGRvw/profile-displayphoto-scale_400_400/B4DZvu5VAOGUAg-/0/1769239565802?e=1771459200&v=beta&t=LseAPd591Le3-pb-BhzUUnn5oUvsFkWG_LQZ-UuFXD8",
            width=170
        )

    with col2:
        st.markdown(
            """
            <div class="cv-card">
                <h3>Valusha Oelofse</h3>
                <p class="small-text">
                Junior Lecturer and Aspiring Data Scientist<br>
                Department of Economics and Finance<br>
                University of the Free State
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            **Profile Summary**<br>
            My passion lies in leveraging data to solve complex financial and 
            business challenges. My experiences encompass data analytics, 
            dashboard creation, data preprocessing, and developing machine learning models. 
            My research focuses on designing a Social Stress 
            Indicator which has sharpened my analytical and problem-solving expertise.
            """
        )

# =================================================
# Experience
# =================================================
elif menu == "Experience":
    st.title("Experience")

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Junior Lecturer</h3>
        <p class="small-text">
        University of the Free State · Contract<br>
        February 2025 – Present<br>
        Bloemfontein, Free State, South Africa (On-site)
        </p>

        <ul>
            <li>Lecturing and supporting undergraduate modules in quantitative and data-oriented subjects</li>
            <li>Designing and delivering tutorials and practical sessions</li>
            <li>Assessment, marking, and academic moderation</li>
            <li>Supporting student development in data analysis and problem-solving skills</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Data Analyst</h3>
        <p class="small-text">
        Interdisciplinary Centre for Digital Futures (ICDF), University of the Free State · Contract<br>
        July 2023 – December 2024<br>
        Bloemfontein, Free State, South Africa (On-site)
        </p>

        <ul>
            <li>Conducted data analysis in support of interdisciplinary research initiatives</li>
            <li>Performed data cleaning, exploratory analysis, and modelling</li>
            <li>Produced analytical outputs and visualisations for research and reporting purposes</li>
            <li>Collaborated with academic and research stakeholders across disciplines</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Intern</h3>
        <p class="small-text">
        Quantify Your Future · Virtual Internship (Powered by SAGEA)<br>
        January 2023 – February 2023<br>
        Remote
        </p>

        <ul>
            <li>Participated in industry-aligned data analytics projects with FirstRand, Absa, and Nedbank</li>
            <li>Gained practical exposure to data framing, exploration, modelling, and visualisation</li>
            <li>Developed core professional skills including critical thinking, collaboration, and communication</li>
            <li>Completed team-based projects facilitated by financial industry partners</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Demonstrator</h3>
        <p class="small-text">
        University of the Free State · Contract<br>
        September 2022 – November 2022<br>
        Bloemfontein, South Africa
        </p>

        <ul>
            <li>Assisted students during practical sessions for module CSIS1644</li>
            <li>Provided academic support and clarification of module content</li>
            <li>Invigilated tests and supported assessment processes</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Demonstrator</h3>
        <p class="small-text">
        University of the Free State · Contract<br>
        February 2022 – July 2022<br>
        Bloemfontein, Free State, South Africa
        </p>

        <ul>
            <li>Supported practical sessions for module CSIS1614</li>
            <li>Answered student queries related to course content and assessments</li>
            <li>Assisted with invigilation and administrative academic duties</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================================================
# Qualifications
# =================================================
elif menu == "Qualifications":
    st.title("Qualifications")

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Master of Commerce (MCom)</h3>
        <p class="small-text">
        Business and Financial Analytics<br>
        University of the Free State<br>
        January 2025 – December 2025
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Bachelor of Commerce Honours (BCom Hons)</h3>
        <p class="small-text">
        Business and Financial Analytics<br>
        University of the Free State<br>
        January 2024 – December 2024
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Bachelor of Commerce (BCom)</h3>
        <p class="small-text">
        Business and Financial Analytics<br>
        University of the Free State<br>
        2021 – 2023
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================================================
# Contact
# =================================================
elif menu == "Contact":
    st.title("Contact")

    st.markdown(
        """
        <div class="cv-card">
            <p>
                <strong>Email:</strong> valusha.oel@gmail.com<br>
                <strong>Institution:</strong> University of the Free State<br>
            </p>
            <a class="linkedin-button" href="https://www.linkedin.com/in/valentinaoelofse/" target="_blank">
                View LinkedIn Profile
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
