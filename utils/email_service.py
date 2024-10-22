import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL_USER")
sender_password = os.getenv("EMAIL_PASSWORD")


def send_email(sender_email: str, sender_password: str, receiver_email: str, subject: str, body: str, smtp_server: str, port: int):
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
        return {"status": "Success", "message": "Email sent successfully"}
    except Exception as e:
        return {"status": "Failed", "message": str(e)}

# print(send_email(
#    sender_email=sender_email,
#    sender_password=sender_password,
#    receiver_email="ali.rammal.4@hotmail.com",
#    subject="Test Email",
#    body="This is a test email sent from Python.",
#    smtp_server="smtp.gmail.com",
#    port=465
# ))
