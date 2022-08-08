'''In order to use this code one needs to allow unsecure connection in Google account'''

import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email"
sender_email = "katarine.belaya@gmail.com"
receiver_email = "katarine.belaya@gmail.com"
password = input("Enter the password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending...")

with smtplib.SMTP_SSL("smtp.google.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success!")