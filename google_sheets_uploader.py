import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()
GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE")

if not GOOGLE_CREDENTIALS_FILE:
    raise ValueError("Missing GOOGLE_CREDENTIALS_FILE! Set it in your .env file.")

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

def upload_to_google_sheets(df, sheet_name):
    """Uploads a DataFrame to Google Sheets."""
    try:
        sheet = client.open(sheet_name).sheet1  # Open the first sheet
        sheet.clear()  # Clears existing content
        sheet.update([df.columns.values.tolist()] + df.values.tolist())  # Uploads data
        print("✅ RSS feed data successfully uploaded to Google Sheets!")
    except Exception as e:
        print(f"❌ Error uploading to Google Sheets: {e}")