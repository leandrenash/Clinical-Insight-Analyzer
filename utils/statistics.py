import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from typing import Dict, Any, Tuple

class StatisticalAnalyzer:
    @staticmethod
    def calculate_basic_stats(data: pd.Series) -> Dict[str, float]:
        """Calculate basic statistical measures"""
        return {
            'mean': float(data.mean()),
            'median': float(data.median()),
            'std': float(data.std()),
            'min': float(data.min()),
            'max': float(data.max())
        }

    @staticmethod
    def perform_ttest(group1: pd.Series, group2: pd.Series) -> Dict[str, float]:
        """Perform Student's t-test"""
        t_stat, p_value = stats.ttest_ind(group1, group2)
        return {
            't_statistic': float(t_stat),
            'p_value': float(p_value)
        }

    @staticmethod
    def perform_anova(df: pd.DataFrame, group_col: str, value_col: str) -> Dict[str, float]:
        """Perform one-way ANOVA"""
        groups = [group for _, group in df.groupby(group_col)[value_col]]
        f_stat, p_value = stats.f_oneway(*groups)
        
        # Perform Tukey's HSD test
        tukey = pairwise_tukeyhsd(df[value_col], df[group_col])
        
        return {
            'f_statistic': float(f_stat),
            'p_value': float(p_value),
            'tukey_results': str(tukey)
        }

    @staticmethod
    def calculate_effect_size(treatment_group: pd.Series, control_group: pd.Series) -> float:
        """Calculate Cohen's d effect size"""
        n1, n2 = len(treatment_group), len(control_group)
        var1, var2 = treatment_group.var(), control_group.var()
        
        pooled_se = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
        cohens_d = (treatment_group.mean() - control_group.mean()) / pooled_se
        
        return float(cohens_d)

    @staticmethod
    def perform_chi_square(df: pd.DataFrame, var1: str, var2: str) -> Dict[str, float]:
        """Perform chi-square test of independence"""
        contingency_table = pd.crosstab(df[var1], df[var2])
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        
        return {
            'chi2_statistic': float(chi2),
            'p_value': float(p_value),
            'degrees_of_freedom': int(dof)
        }
