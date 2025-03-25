import smtplib
import pandas as pd
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# for loading the environment variables
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Loads AI-processed data
df = pd.read_excel("rss_with_scripts.xlsx")

# Assign a virality score (1-10) randomly or via AI (Here, random for simplicity)
import random
df["Virality Score"] = df.apply(lambda _: random.randint(1, 10), axis=1)

# Filter articles with a score above 7
viral_articles = df[df["Virality Score"] > 7]

if not viral_articles.empty:
    # Create email content
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = "🔥 Trending AI-Generated Scripts from RSS Feed"

    # Email body
    body = "Here are the most viral AI-generated content scripts:\n\n"
    for _, row in viral_articles.iterrows():
        body += f"📌 *{row['Title']}*\n🔗 {row['Link']}\n💬 {row['Generated Script']}\n🔥 Virality Score: {row['Virality Score']}\n\n"

    msg.attach(MIMEText(body, "plain"))

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, EMAIL_RECEIVER, msg.as_string())

    print("Email sent successfully with viral articles!")
else:
    print("No highly viral articles to send.")