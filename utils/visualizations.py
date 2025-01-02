import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Dict, Any

class VisualizationGenerator:
    @staticmethod
    def create_treatment_outcome_plot(df: pd.DataFrame) -> go.Figure:
        """Create treatment outcome visualization"""
        fig = px.bar(
            df.groupby('treatment_group')['outcome'].value_counts().unstack(),
            barmode='group',
            title='Treatment Outcomes by Group',
            labels={'value': 'Count', 'treatment_group': 'Treatment Group'}
        )
        fig.update_layout(
            xaxis_title="Treatment Group",
            yaxis_title="Number of Patients",
            legend_title="Outcome"
        )
        return fig

    @staticmethod
    def create_box_plot(df: pd.DataFrame, value_col: str, group_col: str) -> go.Figure:
        """Create box plot for numerical variables"""
        fig = px.box(
            df,
            x=group_col,
            y=value_col,
            title=f'Distribution of {value_col} by {group_col}',
            points="all"
        )
        fig.update_layout(
            xaxis_title=group_col,
            yaxis_title=value_col
        )
        return fig

    @staticmethod
    def create_scatter_plot(
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        color_col: str = None
    ) -> go.Figure:
        """Create scatter plot with optional color grouping"""
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            color=color_col,
            title=f'{y_col} vs {x_col}',
            trendline="ols"
        )
        fig.update_layout(
            xaxis_title=x_col,
            yaxis_title=y_col
        )
        return fig

    @staticmethod
    def create_time_series_plot(
        df: pd.DataFrame,
        time_col: str,
        value_col: str,
        group_col: str = None
    ) -> go.Figure:
        """Create time series plot"""
        fig = px.line(
            df,
            x=time_col,
            y=value_col,
            color=group_col,
            title=f'{value_col} Over Time'
        )
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title=value_col
        )
        return fig

    @staticmethod
    def create_correlation_heatmap(df: pd.DataFrame) -> go.Figure:
        """Create correlation heatmap for numerical variables"""
        correlation_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
        fig = px.imshow(
            correlation_matrix,
            title='Correlation Heatmap',
            aspect='auto'
        )
        fig.update_layout(
            xaxis_title="Variables",
            yaxis_title="Variables"
        )
        return fig
