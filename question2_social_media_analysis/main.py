from data_collection.scrape_books import scrape_books
from data_collection.scrape_demo import scrape_demo_site
from data_collection.rss_parser import parse_rss
from data_processing.clean_books import clean_books
from analysis.stats_analysis import analyze_data
from visualizations.visualize_books import visualize_data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --------- Step 1: Multi-source scraping ---------
books_csv = scrape_books(pages=10)
demo_csv = scrape_demo_site()
rss_csv = parse_rss("https://www.theverge.com/rss/index.xml")

# --------- Step 2: Cleaning ---------
clean_books_csv = clean_books(books_csv)
clean_demo_csv = clean_books(demo_csv)
clean_rss_csv = clean_books(rss_csv)

# --------- Step 3: Analysis ---------
df_books = analyze_data(clean_books_csv)
df_demo = analyze_data(clean_demo_csv)
df_rss = analyze_data(clean_rss_csv)

# --------- Step 4: Visualization ---------
visualize_data(clean_books_csv)
visualize_data(clean_demo_csv)
visualize_data(clean_rss_csv)

# --------- Step 5: Predictive Analysis (books only) ---------
if 'rating' in df_books.columns:
    X = df_books[['rating']]
    y = df_books['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"Regression Coefficient: {model.coef_[0]:.2f}")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

    # Simple recommendation
    def recommend_books(rating, n=5):
        similar_books = df_books[df_books['rating'] == rating].sort_values('price').head(n)
        return similar_books[['title','price','rating']]

    print("Recommended books with 5-star rating:")
    print(recommend_books(5))
