from twilio import rest

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="This is me, Shashank !",
    to="",    # Replace with your phone number
    from_="") # Replace with your Twilio number

print(message.sid)
