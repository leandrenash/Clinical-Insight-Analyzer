import pandas as pd
import numpy as np
from typing import Tuple, Optional

class DataProcessor:
    @staticmethod
    def validate_data(df: pd.DataFrame) -> Tuple[bool, str]:
        """
        Validate uploaded clinical trial data
        """
        if df.empty:
            return False, "Dataset is empty"
        
        required_columns = ['patient_id', 'treatment_group', 'outcome']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return False, f"Missing required columns: {', '.join(missing_columns)}"
            
        if df.duplicated(subset=['patient_id']).any():
            return False, "Duplicate patient IDs found"
            
        return True, "Data validation successful"

    @staticmethod
    def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess clinical trial data
        """
        # Create copy to avoid modifying original
        processed_df = df.copy()
        
        # Handle missing values
        numeric_columns = processed_df.select_dtypes(include=[np.number]).columns
        processed_df[numeric_columns] = processed_df[numeric_columns].fillna(
            processed_df[numeric_columns].mean()
        )
        
        # Handle categorical missing values
        categorical_columns = processed_df.select_dtypes(include=['object']).columns
        processed_df[categorical_columns] = processed_df[categorical_columns].fillna('Unknown')
        
        # Convert dates if present
        date_columns = processed_df.select_dtypes(include=['datetime64']).columns
        for col in date_columns:
            processed_df[col] = pd.to_datetime(processed_df[col])
        
        return processed_df

    @staticmethod
    def generate_summary_statistics(df: pd.DataFrame) -> dict:
        """
        Generate summary statistics for the dataset
        """
        summary = {
            'total_patients': len(df),
            'treatment_groups': df['treatment_group'].value_counts().to_dict(),
            'outcome_distribution': df['outcome'].value_counts().to_dict(),
            'numeric_summaries': df.describe().to_dict()
        }
        return summary
