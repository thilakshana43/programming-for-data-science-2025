# scrape_books.py
import requests
from bs4 import BeautifulSoup
import time
import csv
from urllib.parse import urljoin

BASE = "http://books.toscrape.com/"

def fetch(url, retries=3):
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.text
        except Exception as e:
            if attempt < retries-1:
                time.sleep(1 + attempt)
            else:
                raise

def parse_book(book_soup):
    title = book_soup.h3.a['title']
    price = book_soup.select_one(".price_color").text.strip()
    avail = book_soup.select_one(".availability").text.strip()
    rating = book_soup.select_one("p.star-rating")['class'][1]  # e.g. Three
    return {"title": title, "price": price, "availability": avail, "rating": rating}

def main():
    rows = []
    page = "catalogue/page-1.html"
    while True:
        url = urljoin(BASE, page)
        html = fetch(url)
        soup = BeautifulSoup(html, "html.parser")
        books = soup.select("article.product_pod")
        for b in books:
            rows.append(parse_book(b))
        # find next
        next_li = soup.select_one("li.next a")
        if not next_li:
            break
        page = "catalogue/" + next_li['href']
        time.sleep(1)  # polite delay

    # Save CSV
    keys = rows[0].keys()
    with open("books.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
