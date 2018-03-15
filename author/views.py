from algometica import app

@app.route('/login')
def login():
	return "hello, user!"