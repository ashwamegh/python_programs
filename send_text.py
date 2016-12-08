from twilio import rest

account_sid = "AC503d380f08fe389a6b96b01bd1c72a0d" # Your Account SID from www.twilio.com/console
auth_token  = "7b1ac4f409bbbb9f0f7623c813583814"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="This is me, Shashank !",
    to="+918587099540",    # Replace with your phone number
    from_="+14086229325") # Replace with your Twilio number

print(message.sid)
