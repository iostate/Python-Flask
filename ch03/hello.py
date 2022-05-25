import string
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>', 400


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@app.route('/projects/<project>/<collection>/<name>')
def projects(project, collection, name):
    return '<h1>{}{}{}</h1>'.format(project, collection, name)
