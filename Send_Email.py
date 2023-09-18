import smtplib,ssl
import os


def send_email(email,message_text):
    host = "smtp.gmail.com"
    port = 465

    username = "myburgfrancopython@gmail.com"
    password = os.getenv("PASSWORD")

    reciever = "myburgfranco@gmail.com"

    message = email + "\n" + message_text
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,reciever,message)
