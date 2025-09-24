# data_collection/scrape_demo.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

DATA_DIR = os.path.dirname(__file__)
BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

def scrape_demo_site(delay=1):
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select("div.thumbnail")
    all_items = []

    for prod in products:
        title = prod.select_one("a.title").text.strip()
        price = prod.select_one("h4.price").text.strip().replace('$','')
        description = prod.select_one("p.description").text.strip()
        all_items.append({
            'title': title,
            'price': float(price),
            'description': description
        })
        time.sleep(delay)

    df = pd.DataFrame(all_items)
    csv_path = os.path.join(DATA_DIR, "demo_site.csv")
    df.to_csv(csv_path, index=False)
    print(f"Scraped {len(all_items)} products from demo site. Saved to {csv_path}")
    return csv_path

if __name__ == "__main__":
    scrape_demo_site()
