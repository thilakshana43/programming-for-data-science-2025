# visualizations/visualize_books.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def visualize_data(clean_csv_path):
    df = pd.read_csv(clean_csv_path)
    #Set up a path for save visualizations
    save_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(save_dir, exist_ok=True)

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

    # Interactive scatter plot (books or demo site)
    if 'price' in df.columns and 'title' in df.columns:
        fig = px.scatter(df,
                         x='rating' if 'rating' in df.columns else 'price',
                         y='price',
                         color='title',
                         hover_data=['title'])
        html_path = os.path.join(save_dir, "interactive_plot.html")
        fig.write_html(html_path)
        fig.show()
        print(f"Interactive plot saved to: {html_path}")

    # RSS feed: Top 20 title keywords bar chart
    if {'title', 'link', 'published', 'summary'}.issubset(df.columns):
        df['title_words'] = df['title'].str.lower().str.split()
        all_words = df['title_words'].explode()
        top_words = all_words.value_counts().head(20)

        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_words.values, y=top_words.index)
        plt.title("Top 20 Words in RSS Titles")
        plt.xlabel("Count")
        plt.ylabel("Word")
        plt.tight_layout()
        output_path = os.path.join(save_dir, "rss_keywords.png")
        plt.savefig(output_path)
        plt.show()
        print(f"RSS keywords bar chart saved to: {output_path}")
