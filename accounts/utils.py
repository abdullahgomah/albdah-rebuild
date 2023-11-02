from twilio.rest import Client
from dotenv import load_dotenv
import os 

load_dotenv() 

account_sid = os.environ.get('ACCOUNT_SID') 
auth_token = os.environ.get('AUTH_TOKEN') 

client = Client(account_sid, auth_token)


def send_sms(otp, phone_number):

    message = client.messages \
                    .create(
                        body=f"رمز الدخول هو {otp}",
                        from_='+18589971093',
                        to=phone_number
                    )
