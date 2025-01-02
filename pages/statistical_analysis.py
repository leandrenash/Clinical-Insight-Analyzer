import streamlit as st
import pandas as pd
from utils.statistics import StatisticalAnalyzer

def render_statistical_analysis_page():
    st.title("Statistical Analysis")
    
    if st.session_state.data is None:
        st.warning("Please upload data first!")
        return
    
    df = st.session_state.data
    
    analysis_type = st.selectbox(
        "Select Analysis Type",
        ["Basic Statistics", "T-Test", "ANOVA", "Effect Size", "Chi-Square Test"]
    )
    
    if analysis_type == "Basic Statistics":
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        selected_column = st.selectbox("Select Variable", numeric_columns)
        
        if selected_column:
            stats = StatisticalAnalyzer.calculate_basic_stats(df[selected_column])
            
            st.subheader("Basic Statistics")
            st.write(f"Mean: {stats['mean']:.2f}")
            st.write(f"Median: {stats['median']:.2f}")
            st.write(f"Standard Deviation: {stats['std']:.2f}")
            st.write(f"Minimum: {stats['min']:.2f}")
            st.write(f"Maximum: {stats['max']:.2f}")
    
    elif analysis_type == "T-Test":
        st.subheader("Independent T-Test")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        group_column = st.selectbox("Select Grouping Variable", df.columns)
        value_column = st.selectbox("Select Value Variable", numeric_columns)
        
        groups = df[group_column].unique()
        if len(groups) >= 2:
            group1 = st.selectbox("Select First Group", groups)
            group2 = st.selectbox("Select Second Group", [g for g in groups if g != group1])
            
            result = StatisticalAnalyzer.perform_ttest(
                df[df[group_column] == group1][value_column],
                df[df[group_column] == group2][value_column]
            )
            
            st.write(f"T-Statistic: {result['t_statistic']:.4f}")
            st.write(f"P-Value: {result['p_value']:.4f}")
    
    elif analysis_type == "ANOVA":
        st.subheader("One-way ANOVA")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        group_column = st.selectbox("Select Grouping Variable", df.columns)
        value_column = st.selectbox("Select Value Variable", numeric_columns)
        
        result = StatisticalAnalyzer.perform_anova(df, group_column, value_column)
        
        st.write(f"F-Statistic: {result['f_statistic']:.4f}")
        st.write(f"P-Value: {result['p_value']:.4f}")
        st.text("Tukey's HSD Test Results:")
        st.text(result['tukey_results'])
    
    elif analysis_type == "Effect Size":
        st.subheader("Effect Size Analysis (Cohen's d)")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        group_column = st.selectbox("Select Grouping Variable", df.columns)
        value_column = st.selectbox("Select Value Variable", numeric_columns)
        
        groups = df[group_column].unique()
        if len(groups) >= 2:
            treatment_group = st.selectbox("Select Treatment Group", groups)
            control_group = st.selectbox("Select Control Group", [g for g in groups if g != treatment_group])
            
            effect_size = StatisticalAnalyzer.calculate_effect_size(
                df[df[group_column] == treatment_group][value_column],
                df[df[group_column] == control_group][value_column]
            )
            
            st.write(f"Cohen's d: {effect_size:.4f}")
    
    elif analysis_type == "Chi-Square Test":
        st.subheader("Chi-Square Test of Independence")
        
        categorical_columns = df.select_dtypes(include=['object']).columns
        var1 = st.selectbox("Select First Variable", categorical_columns)
        var2 = st.selectbox("Select Second Variable", [c for c in categorical_columns if c != var1])
        
        result = StatisticalAnalyzer.perform_chi_square(df, var1, var2)
        
        st.write(f"Chi-Square Statistic: {result['chi2_statistic']:.4f}")
        st.write(f"P-Value: {result['p_value']:.4f}")
        st.write(f"Degrees of Freedom: {result['degrees_of_freedom']}")

if __name__ == "__main__":
    render_statistical_analysis_page()
