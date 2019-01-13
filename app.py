import web
from twilio.rest import Client
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
		# Your Account Sid and Auth Token from twilio.com/user/account
		account_sid = "AC9b22a03e6beaa004c00788f5c56bdaee"
		auth_token = "c4219266b011b6a2cf1b5a21010062e2"
		
		from twilio.rest import Client
		client = Client(account_sid, auth_token)

		call = client.calls.create(
		    to="+919870356725",
		    from_="+12243863258",
		    url="https://ramesh-suresh.herokuapp.com/try1.xml"
		)
		
		if not name: 
			name = 'World'
		return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
