import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Load RSS feed data
df = pd.read_excel("rss_feed.xlsx")

# Gemini AI prompt to generate a short content script
def generate_script(article_title, article_summary):
    prompt = f"Create a short, engaging content script based on this news article:\n\nTitle: {article_title}\nSummary: {article_summary}\n\nScript:"
    
    try:
        response = genai.generate_text(model="gemini-pro", prompt=prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating script for {article_title}: {e}")
        return "Error generating script"

# Apply AI script generation to each row
df["Generated Script"] = df.apply(lambda row: generate_script(row["Title"], row["Summary"]), axis=1)

# Save the new Excel file
df.to_excel("rss_with_scripts.xlsx", index=False)

print("✅ AI-generated scripts saved to 'rss_with_scripts.xlsx'.")