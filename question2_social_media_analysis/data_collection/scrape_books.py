# data_collection/scrape_books.py
import requests                 # Used for sending HTTP requests to web pages
from bs4 import BeautifulSoup   # Used for parsing HTML content
import csv                      # Used for saving scraped data into CSV format
import time                     # Used for adding delay between requests
import os                       # Used for handling file paths

# Base URL template for pagination
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
# Header helps mimic a real browser request
HEADERS = {'User-Agent': 'Mozilla/5.0'}
# Directory path where CSV file will be saved
DATA_DIR = os.path.join(os.path.dirname(__file__))


def scrape_books(pages, delay=1):

    all_books = []      # Empty list to store all book records

    # Loop through the number of pages requested
    for page in range(1, pages + 1):
        try:
            # Construct page URL using page number
            url = BASE_URL.format(page)
            # Send GET request to fetch page content
            response = requests.get(url, headers=HEADERS, timeout=5)
            # Raise exception if request failed
            response.raise_for_status()
            # Parse HTML response with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Select all book containers using CSS selector
            books = soup.select('article.product_pod')
            # Extract information for each book
            for book in books:
                title = book.h3.a['title']
                price = book.select_one('p.price_color').text
                price = price.replace('£', '').replace('Â', '').strip()
                rating = book.p['class'][1]
                availability = book.select_one('p.instock.availability').text.strip()

                # Append dictionary of extracted data
                all_books.append({
                    'title': title,
                    'price': float(price),
                    'rating': rating,
                    'availability': availability
                })

            # Add a delay between requests
            time.sleep(delay)
        except Exception as e:
            # Print any error that occurred while scraping a page
            print(f"Error on page {page}: {e}")

    # Save all collected data to a CSV file
    csv_path = os.path.join(DATA_DIR, "books.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price', 'rating', 'availability'])
        writer.writeheader()        # Write CSV header
        writer.writerows(all_books) # Write all rows

    # Print summary
    print(f"Scraped {len(all_books)} books. Saved to {csv_path}")
    return csv_path

# Run script directly
if __name__ == "__main__":
    scrape_books()
