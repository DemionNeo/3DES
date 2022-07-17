import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC84525f2fc6d199f749857ec6e0af8377'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = '88cd5397a3424cd206ba8bf5e46fff40'
client = Client(account_sid, auth_token)
def send_sms(the_body,to):

    message = client.messages.create(
                              body=the_body,
                              from_='+19897109272',
                              to= to
                          )
    return message.sid



