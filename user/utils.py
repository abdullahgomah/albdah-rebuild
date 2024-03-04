from twilio.rest import Client
from dotenv import load_dotenv 
import os 
import random 
import requests

load_dotenv() 

ACCOUNT_SID = os.getenv("ACCOUNT_SID") 
AUTH_TOKEN = os.getenv("AUTH_TOKEN") 

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_otp(to, otp): 
    message = client.messages.create(
                     body=f"مرحباً بكم في مكتب البداح للعقارات. رمز ال دخول هو {otp}", 
                     from_='+18052197512',
                     to=to 
                 )
    
def generate_otp(): 
    return str(random.randint(1000, 9999)) 


def verify_otp(to, otp): 
    url = "https://control.msg91.com/api/v5/flow/"

    payload = {
        "template_id": "65c4ff99d6fc0534a54ffe32",
        "sender_id": "albdah", 
        "short_url": "0",
        "recipients": [
            {
                "mobiles": to,
                "var1": otp
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authkey": "415523A56Obn7kTb65c324a8P1"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)