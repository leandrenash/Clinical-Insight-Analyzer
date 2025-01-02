import streamlit as st
import pandas as pd
from utils.data_processor import DataProcessor

def render_data_upload_page():
    st.title("Data Upload and Validation")
    
    uploaded_file = st.file_uploader(
        "Upload Clinical Trial Data (CSV format)",
        type=['csv']
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            st.subheader("Data Validation")
            is_valid, message = DataProcessor.validate_data(df)
            
            if is_valid:
                st.success(message)
                
                if st.button("Process Data"):
                    processed_df = DataProcessor.preprocess_data(df)
                    st.session_state.data = processed_df
                    
                    summary_stats = DataProcessor.generate_summary_statistics(processed_df)
                    
                    st.subheader("Dataset Summary")
                    st.write(f"Total Patients: {summary_stats['total_patients']}")
                    
                    st.subheader("Treatment Groups Distribution")
                    st.write(summary_stats['treatment_groups'])
                    
                    st.subheader("Outcome Distribution")
                    st.write(summary_stats['outcome_distribution'])
                    
                    st.success("Data processed and stored successfully!")
            else:
                st.error(message)
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    
    if st.session_state.data is not None:
        if st.button("Clear Data"):
            st.session_state.data = None
            st.success("Data cleared successfully!")

if __name__ == "__main__":
    render_data_upload_page()
