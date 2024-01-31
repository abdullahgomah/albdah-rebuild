from twilio.rest import Client
from dotenv import load_dotenv 
import os 
import random 

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