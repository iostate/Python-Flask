import string
from flask import Flask, abort, make_response, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>', 400


#--- REDIRECT
@app.route('/user/<name>/twitter')
def redirect_twitter(name):
    return redirect('http://twitter.com/{}'.format(name))
# -------

# ----- COOKIES


@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

# ------

# ----------USERS


@app.route('/user/<name>')
def user(name):
    if not name:
        abort(404)
    return '<h1>Hello, {} sads!</h1>'.format(name)


# ----- END USERS

@app.route('/projects/<project>/<collection>/<name>')
def projects(project, collection, name):
    return '<h1>{}{}{}</h1>'.format(project, collection, name)
