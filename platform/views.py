from algometica import app

@app.route('/')
@app.route('/index')
def index():
	return 'I am Algometica.'