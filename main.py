import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Clinical Trial Analysis Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("Clinical Trial Data Analysis Platform")
    
    st.markdown("""
    Welcome to the Clinical Trial Data Analysis Platform. This tool provides comprehensive 
    analysis capabilities for clinical trial data, including:
    
    - Statistical Analysis
    - Treatment Effectiveness Visualization
    - Factor Analysis
    - Data Validation and Processing
    
    Please use the sidebar navigation to access different features.
    """)
    
    st.sidebar.title("Navigation")
    
    if 'data' not in st.session_state:
        st.session_state.data = None
    
    st.markdown("""
    ### Getting Started
    1. Upload your clinical trial data using the Data Upload page
    2. Validate and preprocess your data
    3. Explore statistical analyses and visualizations
    4. Generate and export reports
    """)
    
    if st.session_state.data is not None:
        st.success("Data loaded successfully! Use the sidebar to navigate through analysis options.")
        
        st.subheader("Dataset Overview")
        st.dataframe(st.session_state.data.head())
        
        st.subheader("Dataset Statistics")
        st.write(st.session_state.data.describe())
    else:
        st.info("Please upload your data using the Data Upload page to begin analysis.")

if __name__ == "__main__":
    main()
