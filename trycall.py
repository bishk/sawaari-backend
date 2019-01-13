from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9b22a03e6beaa004c00788f5c56bdaee"
auth_token = "c4219266b011b6a2cf1b5a21010062e2"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+918178432260",
    from_="+12243863258",
    url="http://bishk.github.io/sw/xml.xml"
)

print(call.sid)