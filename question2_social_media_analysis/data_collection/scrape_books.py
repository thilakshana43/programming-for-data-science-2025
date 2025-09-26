# data_collection/scrape_books.py
import requests
from bs4 import BeautifulSoup
import csv
import time
import os

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
DATA_DIR = os.path.join(os.path.dirname(__file__))


def scrape_books(pages=10, delay=1):
    all_books = []

    for page in range(1, pages + 1):
        try:
            url = BASE_URL.format(page)
            response = requests.get(url, headers=HEADERS, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            books = soup.select('article.product_pod')
            for book in books:
                title = book.h3.a['title']
                price = book.select_one('p.price_color').text
                price = price.replace('£', '').replace('Â', '').strip()
                rating = book.p['class'][1]
                availability = book.select_one('p.instock.availability').text.strip()

                all_books.append({
                    'title': title,
                    'price': float(price),
                    'rating': rating,
                    'availability': availability
                })

            time.sleep(delay)
        except Exception as e:
            print(f"Error on page {page}: {e}")

    # Save CSV
    csv_path = os.path.join(DATA_DIR, "books.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price', 'rating', 'availability'])
        writer.writeheader()
        writer.writerows(all_books)

    print(f"Scraped {len(all_books)} books. Saved to {csv_path}")
    return csv_path


if __name__ == "__main__":
    scrape_books()
