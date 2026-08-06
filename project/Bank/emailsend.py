# import required modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

#to load content in .env
load_dotenv()

#server config parameters
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSKEY = os.getenv("SENDER_PASSKEY")

def SingleEmailSend(to_email_:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['TO'] = to_email_
    msg['FROM'] = SENDER_EMAIL
    msg['SUBJECT'] = subject
    msg.attach(MIMEText(body,'plain'))

    try:
        #start server
        server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        #start server
        server.starttls()
        #login to server
        server.login(SENDER_EMAIL, PASSKEY)
        #send email
        server.sendmail(SENDER_EMAIL, to_email_, msg.as_string())
        #quite sever
        server.quit()
        return "Successfuly email sent"

    except Exception as e:
        return f"Somthing wrong while sending an email to {to_email_}:{e}"

#read inputs
#email = input("Enter Reciver email address:")
#subject = input("Enter email subject:")
#body = input("enter body")
#print(SingleEmailSend(to_email_=email,subject=subject, body=body))