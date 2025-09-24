# visualizations/visualize_books.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def visualize_data(clean_csv_path):
    df = pd.read_csv(clean_csv_path)
    save_dir = os.path.dirname(clean_csv_path)

    # Price histogram
    if 'price' in df.columns:
        plt.figure(figsize=(10,6))
        sns.histplot(df['price'], bins=30, kde=True)
        plt.title("Price Distribution")
        plt.xlabel("Price")
        plt.ylabel("Count")
        plt.savefig(os.path.join(save_dir, "price_distribution.png"))
        plt.show()

    # Boxplot by rating
    if 'rating' in df.columns:
        plt.figure(figsize=(10,6))
        sns.boxplot(x='rating', y='price', data=df)
        plt.title("Price by Rating")
        plt.savefig(os.path.join(save_dir, "price_by_rating.png"))
        plt.show()

    # Scatter price vs rating
    if 'rating' in df.columns:
        plt.figure(figsize=(10,6))
        sns.scatterplot(x='rating', y='price', data=df)
        plt.title("Rating vs Price")
        plt.savefig(os.path.join(save_dir, "rating_vs_price.png"))
        plt.show()

    # Interactive scatter (books/demo only)
    num_cols = [col for col in ['price','rating'] if col in df.columns]
    if num_cols:
        fig = px.scatter(df, x='rating' if 'rating' in df.columns else 'price',
                         y='price', color='title', hover_data=['title'])
        fig.write_html(os.path.join(save_dir, "interactive_plot.html"))
        fig.show()

    # For RSS feed, plot frequency of words in titles
    if 'title' in df.columns and 'price' not in df.columns:
        df['title_words'] = df['title'].str.split()
        all_words = df['title_words'].explode()
        top_words = all_words.value_counts().head(20)
        plt.figure(figsize=(10,6))
        sns.barplot(x=top_words.values, y=top_words.index)
        plt.title("Top 20 Words in RSS Titles")
        plt.xlabel("Count")
        plt.ylabel("Word")
        plt.show()
