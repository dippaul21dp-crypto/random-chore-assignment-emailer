"""
==============================================================================
Project: Random Chore Assignment Emailer
Context: Level 1, Term II (1-2) Undergraduate Python Course Project
Author : Dip Paul
Status : Educational / Experimental Prototype
==============================================================================
"""

import os
import random
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "pythonproject83@gmail.com")
SENDER_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "")

# Household members pool
HOUSEHOLD_MEMBERS = [
    {"name": "Dip Paul", "email": "dippaul21dp@gmail.com"},
    {"name": "Elsewear", "email": "elsewear6@gmail.com"},
    {"name": "Rudro", "email": "rudrwcvc@gmail.com"},
    {"name": "Emon", "email": "rahmanemon261@gmail.com"},
    {"name": "Shagor", "email": "shagor@gmail.com"},
]

# Chores pool
CHORES = [
    "Wash dishes",
    "Take out the trash",
    "Vacuum the living room",
    "Clean the bathroom",
    "Mow the lawn",
]

def send_email(subject, body, to_email):
    """Dispatches an email via Gmail SMTP."""
    if not SENDER_PASSWORD:
        print(f"[PREVIEW] Email to {to_email} skipped: SENDER_APP_PASSWORD not set in .env")
        return

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, message.as_string())
        print(f"[SUCCESS] Email sent to {to_email}")
    except Exception as e:
        print(f"[ERROR] Failed to send email to {to_email}: {e}")

def assign_all_chores():
    """Randomly distributes all tasks across registered household members."""
    print("\n--- Assigning Chores to Household Members ---")
    shuffled_chores = random.sample(CHORES, len(CHORES))

    for i, member in enumerate(HOUSEHOLD_MEMBERS):
        assigned_chore = shuffled_chores[i % len(shuffled_chores)]
        subject = "Chore Assignment"
        body = (
            f"Dear {member['email']},\n\n"
            f"You have been assigned the chore: {assigned_chore}.\n\n"
            f"Best regards,\n"
            f"The Automated Chore Assignment System"
        )
        print(f"Assigning '{assigned_chore}' to {member['name']} ({member['email']})...")
        send_email(subject, body, member["email"])
        time.sleep(1)

if __name__ == "__main__":
    print("========================================")
    print("    Random Chore Assignment Emailer     ")
    print("========================================")
    assign_all_chores()
