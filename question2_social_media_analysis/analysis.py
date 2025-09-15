# analysis.py
import pandas as pd
import numpy as np
from scipy import stats

def descriptive_stats(df, col='price'):
    return {
        'count': int(df[col].count()),
        'mean': float(df[col].mean()),
        'median': float(df[col].median()),
        'std': float(df[col].std()),
        'min': float(df[col].min()),
        'max': float(df[col].max())
    }

def detect_outliers_zscore(df, col='price', threshold=3.0):
    z = np.abs(stats.zscore(df[col].fillna(df[col].mean())))
    return df[z > threshold]

def correlation(df, col1='price', col2='rating_num'):
    return df[[col1, col2]].corr().iloc[0,1]
