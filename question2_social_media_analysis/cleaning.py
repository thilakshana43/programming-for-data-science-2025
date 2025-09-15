# cleaning.py
import pandas as pd
import re
from datetime import datetime

def load_books(path="books.csv"):
    df = pd.read_csv(path)
    # price: remove currency sign
    df['price'] = df['price'].str.replace(r'[^0-9\.]', '', regex=True).astype(float)
    # rating: map words to numbers
    mapping = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    df['rating_num'] = df['rating'].map(mapping).fillna(0).astype(int)
    # availability: extract numeric stock if present
    df['in_stock'] = df['availability'].str.contains("In stock")
    df.drop_duplicates(subset=['title'], inplace=True)
    df['scraped_at'] = datetime.utcnow()
    return df

def extract_keywords(text):
    # simple keyword extraction: tokens longer than 3 chars
    tokens = re.findall(r"\w+", text.lower())
    keywords = [t for t in tokens if len(t) > 3]
    return list(set(keywords))
