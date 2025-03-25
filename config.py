import os
from dotenv import load_dotenv

#environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY! Please set it in your environment.")

# RSS Feed URL
RSS_FEED_URL = os.environ.get("RSS_FEED_URL")
if not RSS_FEED_URL:
    raise ValueError("Missing RSS_FEED_URL! Please set it in your environment.")

GOOGLE_SHEET_NAME = os.environ.get("GOOGLE_SHEET_NAME", "DefaultSheet")

# Email Credentials
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")  # Receiver's email

#required environment variables need to be set
if not EMAIL_USER or not EMAIL_PASSWORD:
    raise ValueError("Missing email credentials! Please set them in your environment.")

if not EMAIL_RECEIVER:
    raise ValueError("Missing receiver email! Please set EMAIL_RECEIVER in your environment.")