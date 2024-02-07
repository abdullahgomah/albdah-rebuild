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
    return str(random.randint(10000, 99999)) 


def verify_otp(): 

    url = "https://control.msg91.com/api/v5/flow/"

    payload = {
        "template_id": "65c32758d6fc055098443712",
        "short_url": "0",
        "recipients": [
            {
                "mobiles": "+201508420041",
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