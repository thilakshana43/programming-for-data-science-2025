# analysis/stats_analysis.py
import pandas as pd
from scipy.stats import pearsonr


def analyze_data(clean_csv_path):
    df = pd.read_csv(clean_csv_path)
    print(f"\n--- Analyzing {clean_csv_path} ---\n")

    # Display price statistics if column exists
    if 'price' in df.columns:
        print("Price stats:\n", df['price'].describe())

    # Calculate correlation between price and rating (for books)
    if 'rating' in df.columns:
        print("Rating stats:\n", df['rating'].describe())
        corr, _ = pearsonr(df['price'], df['rating'])
        print(f"Correlation between price and rating: {corr:.2f}")

    # Frequency distribution for categorical columns
    cat_cols = [col for col in df.columns if df[col].dtype == 'object']
    for col in cat_cols:
        print(f"\nFrequency distribution for {col}:\n", df[col].value_counts().head(10))

    # Outlier detection for price
    if 'price' in df.columns:
        Q1 = df['price'].quantile(0.25)
        Q3 = df['price'].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df['price'] < Q1 - 1.5 * IQR) | (df['price'] > Q3 + 1.5 * IQR)]
        print(f"Detected {len(outliers)} price outliers")

    return df
