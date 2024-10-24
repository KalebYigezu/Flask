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

-------------------------------------------------
     Is it New Year app

import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    newyear = now.month == 1 and now.day == 1
    return render_template("index.html", newyear=newyear)

app.run()

<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
{% if newyear %}
     <h1> It is {{ newyear }} it is a New Year</h1>
{% else %}
     <h1> It is not new year</h1>
{% endif %}
</body>
</html>
 ---------------------------------------------
       Using url

 import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/more')
def more():
    return render_template("more.html")

app.run()

#index.html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
     <h1> First Page</h1>
    <p>I love Kitfo. I love Misir. I love Dinich. I love Kitfo. I love Misir.
        I love Dinich. I love Kitfo. I love Misir. I love Dinich.I love Kitfo.
        I love Misir. I love Dinich. I love Kitfo. I love Misir. I love Dinich.  </p>
<a href="{{ url_for('more') }}">Go to second page</a>
</body>
</html>

#more.html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
     <h1> Second Page</h1>
    <p>I love Kitfo. I love Misir. I love Dinich. I love Kitfo. I love Misir.
        I love Dinich. I love Kitfo. I love Misir. I love Dinich.I love Kitfo.
        I love Misir. I love Dinich. I love Kitfo. I love Misir. I love Dinich.  </p>
<a href="{{ url_for('index') }}">Go to first page</a>
</body>
</html>
-----------------------------------------------------------------------------------
             Using Layout

import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/more')
def more():
    return render_template("more.html")


app.run()

#layout.html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
     <h1> {% block heading %}{% endblock %} </h1>
     {% block body %}
     {% endblock %}
</body>
</html>

 #index.html
 {% extends "layout.html" %}

{% block heading %}
     First Page
{% endblock %}

{% block body %}
    <p>I love Kitfo. I love Misir. I love Dinich. I love Kitfo. I love Misir.
        I love Dinich. I love Kitfo. I love Misir. I love Dinich.I love Kitfo.
        I love Misir. I love Dinich. I love Kitfo. I love Misir. I love Dinich.  </p>

<a href="{{ url_for('more') }}">Go to second page</a>


{% endblock %}

#more
{% extends "layout.html" %}

{% block heading %}
     Second Page
{% endblock %}

{% block body %}
    <p>I love Kitfo. I love Misir. I love Dinich. I love Kitfo. I love Misir.
        I love Dinich. I love Kitfo. I love Misir. I love Dinich.I love Kitfo.
        I love Misir. I love Dinich. I love Kitfo. I love Misir. I love Dinich.  </p>

<a href="{{ url_for('index') }}">Go to first page</a>


{% endblock %}








