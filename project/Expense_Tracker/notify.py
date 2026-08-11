# notify.py
# sends email notification using gmail id and app passkey
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSKEY = os.getenv("SENDER_PASSKEY")


def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, PASSKEY)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print("Email notification sent!")
    except Exception as e:
        print("Email not sent:", e)
