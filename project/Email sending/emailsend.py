##import required modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#server config parameters
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
SENDER_EMAIL="Your email"
PASSKEY="YOU app passkey"

def sinlrEmailSend(to_email:str, subject:str, body:str):
    msg=MIMEMultipart()
    msg['To']=to_email
    msg['From']=SENDER_EMAIL
    msg['Subject']=subject
    msg.attach(MIMEMultipart(body,'plain'))
    try:
        #start server
        server=smtp.SMTP(SMTP_SERVER, SMTP_PORT)
        #start server
        server.starttls()
        #login to server
        server.login(SENDER_EMAIL, PASSKEY)
        #send email 
        server.sendmail(SENDER_EMAIL, to_email,msg.as_string())
        #quit server
        server.quit()
    except Exception as e:
        return (f"Something wrong sending am emial to{to email}:{e}")
#read inputs
email=input("Enter Receiver email address:")
subject=input("Enter email subject:")
body=input("Enter email body:")
print(singleEmailSend(to_email=email, subject=subject, body=body))