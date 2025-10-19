# data_collection/rss_parser.py
import feedparser       # Library for parsing RSS/XML feeds
import pandas as pd
import os

DATA_DIR = os.path.dirname(__file__)


def parse_rss(url):
    feed = feedparser.parse(url)    # Parse RSS feed URL
    items = []

    # Loop through each entry in the RSS feed
    for entry in feed.entries:
        title = entry.title                         # Article title
        link = entry.link                           # URL to article
        published = entry.get('published', None)    # Published date (if available)
        summary = entry.get('summary', None)        # Short description

        # Store data in a dictionary
        items.append({
            'title': title,
            'link': link,
            'published': published,
            'summary': summary
        })

    # Save parsed feed to CSV file
    df = pd.DataFrame(items)
    csv_path = os.path.join(DATA_DIR, "rss_data.csv")
    df.to_csv(csv_path, index=False)
    print(f"RSS feed parsed and saved to {csv_path}")
    return csv_path


if __name__ == "__main__":
    rss_url = "https://www.theverge.com/rss/index.xml"  # Example RSS feed
    parse_rss(rss_url)
