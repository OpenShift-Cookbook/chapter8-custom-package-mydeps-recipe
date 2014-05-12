from flask import Flask
import msgs.hello as hello

app = Flask(__name__)

@app.route('/')
def index():
	return hello.hello()

if __name__ == '__main__':
	app.run(debug=True)