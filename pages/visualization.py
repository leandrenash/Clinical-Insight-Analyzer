import streamlit as st
from utils.visualizations import VisualizationGenerator

def render_visualization_page():
    st.title("Data Visualization")
    
    if st.session_state.data is None:
        st.warning("Please upload data first!")
        return
    
    df = st.session_state.data
    
    plot_type = st.selectbox(
        "Select Visualization Type",
        ["Treatment Outcomes", "Box Plot", "Scatter Plot", "Time Series", "Correlation Heatmap"]
    )
    
    if plot_type == "Treatment Outcomes":
        st.subheader("Treatment Outcomes Visualization")
        fig = VisualizationGenerator.create_treatment_outcome_plot(df)
        st.plotly_chart(fig)
    
    elif plot_type == "Box Plot":
        st.subheader("Box Plot")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        categorical_columns = df.select_dtypes(include=['object']).columns
        
        value_col = st.selectbox("Select Value Variable", numeric_columns)
        group_col = st.selectbox("Select Grouping Variable", categorical_columns)
        
        fig = VisualizationGenerator.create_box_plot(df, value_col, group_col)
        st.plotly_chart(fig)
    
    elif plot_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        x_col = st.selectbox("Select X Variable", numeric_columns)
        y_col = st.selectbox("Select Y Variable", [col for col in numeric_columns if col != x_col])
        
        color_col = st.selectbox(
            "Select Color Variable (optional)",
            ["None"] + list(df.columns)
        )
        
        fig = VisualizationGenerator.create_scatter_plot(
            df,
            x_col,
            y_col,
            color_col if color_col != "None" else None
        )
        st.plotly_chart(fig)
    
    elif plot_type == "Time Series":
        st.subheader("Time Series Plot")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        date_columns = df.select_dtypes(include=['datetime64']).columns
        
        if len(date_columns) == 0:
            st.warning("No datetime columns found in the dataset")
            return
        
        time_col = st.selectbox("Select Time Variable", date_columns)
        value_col = st.selectbox("Select Value Variable", numeric_columns)
        group_col = st.selectbox(
            "Select Grouping Variable (optional)",
            ["None"] + list(df.select_dtypes(include=['object']).columns)
        )
        
        fig = VisualizationGenerator.create_time_series_plot(
            df,
            time_col,
            value_col,
            group_col if group_col != "None" else None
        )
        st.plotly_chart(fig)
    
    elif plot_type == "Correlation Heatmap":
        st.subheader("Correlation Heatmap")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        selected_columns = st.multiselect(
            "Select Variables",
            numeric_columns,
            default=list(numeric_columns)[:6]
        )
        
        if selected_columns:
            fig = VisualizationGenerator.create_correlation_heatmap(df[selected_columns])
            st.plotly_chart(fig)
    
    # Add export functionality
    if st.button("Export Visualization"):
        st.markdown(
            "To save the visualization, use the camera icon that appears "
            "when hovering over the top-right corner of the plot."
        )

if __name__ == "__main__":
    render_visualization_page()
