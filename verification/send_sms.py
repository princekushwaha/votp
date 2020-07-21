from twilio.rest import Client
import asyncio

account_sid = 'ACbe2d18e88e35ec08f46726913c694bf8'
auth_token = 'bfe9d618169172c0eb83ac0d3c833878'
client = Client(account_sid, auth_token)


def send_sms(body, to, frm = '+12057518302'):  
    account_sid = 'ACbe2d18e88e35ec08f46726913c694bf8'
    auth_token = 'bfe9d618169172c0eb83ac0d3c833878'
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
                    .create(
                        body=body,
                        from_=str(frm),
                        to='+91' + str(to)
                 )
    except:
        print("Failed")
   
   