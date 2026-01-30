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
        color: white;
        padding: 0.45rem 0.9rem;
        text-decoration: none;
        border-radius: 4px;
        font-weight: 500;
    }
    .linkedin-button:hover {
        background-color: #3b2366;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Sidebar navigation
# -------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Select section",
    [
        "Academic Profile",
        "Teaching Experience",
        "Research and Methods",
        "Qualifications",
        "Skills and Tools",
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
            "https://cdn.pixabay.com/photo/2017/08/30/07/52/portrait-2695584_640.jpg",
            width=170
        )

    with col2:
        st.markdown(
            """
            <div class="cv-card">
                <h3> Valusha Oelofse</h3>
                <p class="small-text">
                Junior Lecturer and Aspiring Data Scientist<br>
                Department of Economics and Finance<br>
                University of the Free Sate
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            **Profile Summary**

            My passion lies in leveraging data to solve complex financial and 
            business challenges. My experiences encompass data analytics, 
            dashboard creation, data preprocessing, and developing machine learning classification models. 
            My research focus on designing a Social Stress 
            Indicator which has further sharpened my analytical and problem-solving expertise.
            """
        )

        st.markdown(
            """
            <a class="linkedin-button" href="https://www.linkedin.com/in/valentinaoelofse/" target="_blank">
            View LinkedIn Profile
            </a>
            """,
            unsafe_allow_html=True
        )

# =================================================
# Teaching Experience
# =================================================
elif menu == "Teaching Experience":
    st.title("Teaching Experience")

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Junior Lecturer</h3>
        <p class="small-text">
        University of Science | 2021 – Present
        </p>

        <ul>
            <li>Lecturing and tutoring undergraduate modules in research methods and data analysis</li>
            <li>Designing and delivering practical sessions focused on applied statistics</li>
            <li>Assessment design, marking, and academic moderation</li>
            <li>Supervision of undergraduate research projects</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Ad Hoc Teaching Assistant</h3>
        <p class="small-text">
        University of Science | 2018 – 2020
        </p>

        <ul>
            <li>Assisted with tutorials and practical sessions</li>
            <li>Provided academic support and consultation to students</li>
            <li>Assisted with grading and feedback</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================================================
# Research and Methods
# =================================================
elif menu == "Research and Methods":
    st.title("Research and Methods")

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Research Interests</h3>

        <ul>
            <li>Applied data science in STEM education</li>
            <li>Statistical modelling and inference</li>
            <li>Time-series analysis</li>
            <li>Machine learning applications in academic research</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">Methodological Expertise</h3>

        <ul>
            <li>Exploratory data analysis and visualisation</li>
            <li>Regression and multivariate analysis</li>
            <li>Model validation and interpretation</li>
            <li>Reproducible research workflows</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================================================
# Qualifications
# =================================================
elif menu == "Qualifications":
    st.title("Academic Qualifications")

    st.markdown(
        """
        <div class="cv-card">
        <h3 class="section-title">PhD in Astrophysics</h3>
        <p class="small-text">University of Science | 2018</p>
        </div>

        <div class="cv-card">
        <h3 class="section-title">MSc in Physics</h3>
        <p class="small-text">University of Science | 2014</p>
        </div>

        <div class="cv-card">
        <h3 class="section-title">BSc (Hons) in Physics</h3>
        <p class="small-text">University of Science | 2012</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================================================
# Skills and Tools
# =================================================
elif menu == "Skills and Tools":
    st.title("Skills and Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="cv-card">
            <h3 class="section-title">Technical Skills</h3>

            <ul>
                <li>Statistical analysis</li>
                <li>Data science methodologies</li>
                <li>Machine learning</li>
                <li>Academic writing and peer review</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="cv-card">
            <h3 class="section-title">Tools and Technologies</h3>

            <ul>
                <li>Python (pandas, numpy, scikit-learn)</li>
                <li>R (tidyverse)</li>
                <li>SQL</li>
                <li>LaTeX</li>
                <li>Git and reproducible workflows</li>
            </ul>
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
        <strong>Email:</strong> jane.doe@example.com<br>
        <strong>Institution:</strong> University of Science<br>
        <strong>Office Hours:</strong> By appointment
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
