# data_processing/clean_books.py
import pandas as pd
import os

DATA_DIR = os.path.dirname(__file__)

def clean_books(csv_path):
    df = pd.read_csv(csv_path)  # Load raw CSV into DataFrame
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    # Normalize text (convert to lowercase and remove spaces)
    df['title'] = df['title'].str.lower().str.strip()
    # Convert textual ratings to numeric (only for book dataset)
    if 'rating' in df.columns:
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        df['rating'] = df['rating'].map(rating_map)
    # Add boolean flag for stock availability (books only)
    if 'availability' in df.columns:
        df['in_stock'] = df['availability'].apply(lambda x: 'In stock' in x)
    # Remove rows with invalid or missing prices
    if 'price' in df.columns:
        df = df[df['price'] > 0]
    # Convert published dates to consistent datetime format (for RSS data)
    if 'published' in df.columns:
        df['published'] = pd.to_datetime(df['published'], errors='coerce')
    # Save cleaned CSV
    clean_path = os.path.join(DATA_DIR, os.path.basename(csv_path).replace(".csv", "_clean.csv"))
    df.to_csv(clean_path, index=False)

    print(f"Cleaned data saved to {clean_path}")
    return clean_path
