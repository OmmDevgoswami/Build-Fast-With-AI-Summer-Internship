import requests
import smtplib
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = "dummy.email@gmail.com"
PASSWORD = "password321"
telegram_key = os.getenv("TELEGRAM_API")
botID = os.getenv("BOT_ID")

with open("Built Fast with AI\\Message Creation\\message_details.txt", "r" , encoding="cp1252") as file:
    values = file.readlines()
    
messages = values[1:]    

for _ in messages:
    parts = _.strip().split(",", 1)
    recipient_email, message = parts[0].strip(), parts[1].strip()
    
    
    with smtplib.SMTP("smtp.gmail.com", port = 587) as emailSender:
                emailSender.starttls()
                emailSender.login(user = EMAIL, password = PASSWORD)
                emailSender.sendmail(from_addr = EMAIL,
                                    to_addrs = recipient_email,
                                    msg = f"Subject: Built Fast with AI !! \n\n{message}"
                )
    
    encoded_message = urllib.parse.quote(message)    
    send_text = f'https://api.telegram.org/bot{telegram_key}/sendMessage?chat_id={botID}&parse_mode=HTML&text={urllib.parse.quote(encoded_message)}'
    response = requests.get(send_text)

print("All Messages Sent Succesfully")