import feedparser
from config import RSS_FEED_URL

def fetch_latest_article():
    feed = feedparser.parse(RSS_FEED_URL)
    if feed.entries:
        latest_article = feed.entries[0]  # Get the latest article
        return {
            "title": latest_article.title,
            "link": latest_article.link,
            "summary": latest_article.summary
        }
    return None

if __name__ == "__main__":
    print(fetch_latest_article())  # Test the function