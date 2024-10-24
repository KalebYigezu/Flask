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

--------------------------------------------
         Basics ++

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

app.run()

--------------------------------------------
        Advance

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    headline = "Hello"
    return render_template("index.html", headline=headline)
    # html will take the headline variable in its {{ }} which
    # is it's Jinja2 templating language

@app.route('/bye')
def bye():
    headline = "Bye!"
    return render_template("index.html", headline=headline)

app.run()








