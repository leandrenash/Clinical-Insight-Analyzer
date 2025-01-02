import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from utils.visualizations import VisualizationGenerator

def render_factor_analysis_page():
    st.title("Factor Analysis")
    
    if st.session_state.data is None:
        st.warning("Please upload data first!")
        return
    
    df = st.session_state.data
    
    analysis_type = st.selectbox(
        "Select Analysis Type",
        ["Correlation Analysis", "Principal Component Analysis"]
    )
    
    if analysis_type == "Correlation Analysis":
        st.subheader("Correlation Analysis")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        selected_columns = st.multiselect(
            "Select Variables for Correlation Analysis",
            numeric_columns,
            default=list(numeric_columns)[:4]
        )
        
        if selected_columns:
            correlation_matrix = df[selected_columns].corr()
            
            st.subheader("Correlation Matrix")
            st.dataframe(correlation_matrix.style.format("{:.2f}"))
            
            fig = VisualizationGenerator.create_correlation_heatmap(df[selected_columns])
            st.plotly_chart(fig)
    
    elif analysis_type == "Principal Component Analysis":
        st.subheader("Principal Component Analysis (PCA)")
        
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        selected_columns = st.multiselect(
            "Select Variables for PCA",
            numeric_columns,
            default=list(numeric_columns)[:4]
        )
        
        if selected_columns:
            n_components = st.slider(
                "Number of Components",
                min_value=2,
                max_value=len(selected_columns),
                value=min(3, len(selected_columns))
            )
            
            # Prepare data for PCA
            X = df[selected_columns]
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            # Perform PCA
            pca = PCA(n_components=n_components)
            X_pca = pca.fit_transform(X_scaled)
            
            # Display explained variance ratio
            explained_variance = pca.explained_variance_ratio_
            cumulative_variance = np.cumsum(explained_variance)
            
            st.subheader("Explained Variance Ratio")
            for i, var in enumerate(explained_variance):
                st.write(f"PC{i+1}: {var:.4f} ({cumulative_variance[i]:.4f} cumulative)")
            
            # Create PCA component plot
            if n_components >= 2:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=X_pca[:, 0],
                    y=X_pca[:, 1],
                    mode='markers',
                    text=df.index,
                    name='Samples'
                ))
                fig.update_layout(
                    title='PCA Plot (First Two Components)',
                    xaxis_title=f'PC1 ({explained_variance[0]:.2%} variance)',
                    yaxis_title=f'PC2 ({explained_variance[1]:.2%} variance)'
                )
                st.plotly_chart(fig)
            
            # Display component loadings
            loadings = pd.DataFrame(
                pca.components_.T,
                columns=[f'PC{i+1}' for i in range(n_components)],
                index=selected_columns
            )
            st.subheader("Component Loadings")
            st.dataframe(loadings.style.format("{:.4f}"))

if __name__ == "__main__":
    render_factor_analysis_page()
