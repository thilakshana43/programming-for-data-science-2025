# data_collection/rss_parser.py
import feedparser
import pandas as pd
import os

DATA_DIR = os.path.dirname(__file__)


def parse_rss(url):
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.get('published', None)
        summary = entry.get('summary', None)

        items.append({
            'title': title,
            'link': link,
            'published': published,
            'summary': summary
        })

    df = pd.DataFrame(items)
    csv_path = os.path.join(DATA_DIR, "rss_data.csv")
    df.to_csv(csv_path, index=False)
    print(f"RSS feed parsed and saved to {csv_path}")
    return csv_path


if __name__ == "__main__":
    rss_url = "https://www.theverge.com/rss/index.xml"  # Example RSS feed
    parse_rss(rss_url)
