import feedparser
import pandas as pd

# RSS feed URL
rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"

# Parse the feed
feed = feedparser.parse(rss_url)

# Extract data
articles = []
for entry in feed.entries:
    articles.append({
        "Title": entry.title,
        "Link": entry.link,
        "Published": entry.published,
        "Summary": entry.summary
    })

# Convert to DataFrame
df = pd.DataFrame(articles)

# Save to Excel
df.to_excel("rss_feed.xlsx", index=False)

print("RSS feed saved to rss_feed.xlsx")