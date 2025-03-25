import os
import feedparser
import pandas as pd
from dotenv import load_dotenv
from ai_content_generator import generate_script
from google_sheets_uploader import upload_to_google_sheets

# Load environment variables
load_dotenv()

# Fetch RSS Feed URL
RSS_FEED_URL = os.getenv("RSS_FEED_URL")
if not RSS_FEED_URL:
    raise ValueError("Missing RSS_FEED_URL! Please set it in your environment.")

# Fetch Google Sheet name
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "Import_RSS_Feed")

# Parse RSS feed
feed = feedparser.parse(RSS_FEED_URL)

# Extracts articles
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

# Generate AI scripts for articles
df["Generated Script"] = df.apply(lambda row: generate_script(row["Title"], row["Summary"]), axis=1)

# Save to Excel
df.to_excel("rss_with_scripts.xlsx", index=False)

print("✅ AI-generated scripts saved to 'rss_with_scripts.xlsx'.")

# Upload to Google Sheets
try:
    upload_to_google_sheets(df, GOOGLE_SHEET_NAME)
except Exception as e:
    print(f"❌ Error uploading to Google Sheets: {e}")