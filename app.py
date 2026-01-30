elif menu == "Teaching & Data Portfolio":
    st.title("Teaching and Data Portfolio")

    st.markdown(
        """
        This section provides an overview of teaching contributions,
        methodological expertise, and applied data analysis competencies.
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # -------------------------------
    # Teaching
    # -------------------------------
    with col1:
        st.subheader("Teaching Experience")

        st.markdown(
            """
            **Modules Taught / Assisted**
            - Research Methods and Data Analysis
            - Introduction to Statistics
            - Data Science for STEM
            - Quantitative Methods

            **Teaching Activities**
            - Lectures and tutorials
            - Curriculum development
            - Student assessment and moderation
            - Academic supervision
            """
        )

    # -------------------------------
    # Research & Data
    # -------------------------------
    with col2:
        st.subheader("Research and Data Expertise")

        st.markdown(
            """
            **Methods and Techniques**
            - Exploratory data analysis
            - Statistical modelling
            - Time-series analysis
            - Machine learning (supervised and unsupervised)

            **Tools**
            - Python (pandas, numpy, scikit-learn)
            - R (tidyverse, ggplot2)
            - SQL
            - LaTeX and academic publishing workflows
            """
        )

    st.markdown("---")

    # -------------------------------
    # Example analytical workflow
    # -------------------------------
    st.subheader("Example Analytical Workflow")

    st.markdown(
        """
        The typical analytical workflow applied in both research and teaching contexts includes:
        """
    )

    workflow = pd.DataFrame({
        "Step": [
            "Problem formulation",
            "Data collection",
            "Data cleaning and preprocessing",
            "Exploratory data analysis",
            "Model selection and estimation",
            "Validation and interpretation",
            "Reporting and visualisation"
        ],
        "Description": [
            "Define research questions and hypotheses",
            "Acquire data from primary or secondary sources",
            "Handle missing values, outliers, and inconsistencies",
            "Summarise and visualise key patterns",
            "Apply appropriate statistical or ML models",
            "Assess robustness and interpret results",
            "Communicate findings in academic format"
        ]
    })

    st.dataframe(workflow, use_container_width=True)

    with st.expander("Application in Teaching"):
        st.write(
            "This workflow is integrated into coursework and practical sessions "
            "to ensure students develop applied, reproducible data analysis skills."
        )
