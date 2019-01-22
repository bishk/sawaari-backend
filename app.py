import web
from twilio.rest import Client
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
		# Your Account Sid and Auth Token from twilio.com/user/account
		account_sid = "AC225e0a9803dcf2988bbe58434acff502"
		auth_token = "40187b4079257e68d7d27c99613c4ab8"
		
		from twilio.rest import Client
		client = Client(account_sid, auth_token)

		call = client.calls.create(
		    to="+918178432260",
		    from_="+19193354986",
		    url="https://ramesh-suresh.herokuapp.com/try1.xml"
		)
		
		if not name: 
			name = 'World'
		return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
