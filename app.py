from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

app.run()

       Basics
-------------------------------------------------
       Basics + 

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello!"


@app.route('/david')
def david():
    return "Hello David!"

@app.route("/<name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello {name}<h1>"

app.run()
