from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5bde985dc1315e786443951fc0f487ed"
# Your Auth Token from twilio.com/console
auth_token  = "bfb1912f28ab229bd19a0c0ce7529939"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917780467063", 
    from_="+15105737453",
    body="Hello i am badulla sending from Python!")

print(message.sid)
