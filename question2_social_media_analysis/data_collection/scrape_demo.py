# data_collection/scrape_demo.py
import requests                 # To fetch HTML content
from bs4 import BeautifulSoup   # To parse HTML and extract elements
import pandas as pd             # For structured data handling and CSV export
import time                     # Delay handling
import os                       # file path handling

DATA_DIR = os.path.dirname(__file__)        # Current script folder path
BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"       # Demo site

def scrape_demo_site(delay=1):
    response = requests.get(BASE_URL)                               # Send HTTP request
    soup = BeautifulSoup(response.text, "html.parser")      # Parse HTML response

    # Each product is in a 'div.thumbnail' container
    products = soup.select("div.thumbnail")
    all_items = []

    # Loop through each product and extract info
    for prod in products:
        title = prod.select_one("a.title").text.strip()                                 # Product title
        price = prod.select_one("h4.price").text.strip().replace('$','')    # Remove $
        description = prod.select_one("p.description").text.strip()                     # Product description
        # Add extracted info to list
        all_items.append({
            'title': title,
            'price': float(price),
            'description': description
        })
        time.sleep(delay)       # polite delay between each product

    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(all_items)
    csv_path = os.path.join(DATA_DIR, "demo_site.csv")
    df.to_csv(csv_path, index=False)
    print(f"Scraped {len(all_items)} products from demo site. Saved to {csv_path}")
    return csv_path

if __name__ == "__main__":
    scrape_demo_site()
