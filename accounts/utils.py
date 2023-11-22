from twilio.rest import Client
from dotenv import load_dotenv
import os 

load_dotenv() 

# account_sid = os.environ.get('ACCOUNT_SID') 
account_sid = "AC5611d27d7f84054aa3b3c4e0fb8247fb" 

# auth_token = os.environ.get('AUTH_TOKEN') 
auth_token = "8847378e5c3e1563ebf7d1c249ad3eca" 

client = Client(account_sid, auth_token)


def send_sms(otp, phone_number):

    message = client.messages \
                    .create(
                        body=f"رمز الدخول هو {otp}",
                        from_='+18589971093',
                        to=phone_number
                    )
