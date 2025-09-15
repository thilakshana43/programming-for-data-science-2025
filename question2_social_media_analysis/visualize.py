# visualize.py
import matplotlib.pyplot as plt
import plotly.express as px

def price_histogram(df):
    plt.figure()
    df['price'].hist(bins=30)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.savefig("price_histogram.png")

def rating_vs_price(df):
    fig = px.scatter(df, x='rating_num', y='price', trendline='ols', title='Rating vs Price')
    fig.write_html("rating_vs_price.html")
