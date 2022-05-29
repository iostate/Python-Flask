from flask import request, Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent), 400


@app.route('/projects/<project>/<collection>/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@app.route('/projects/<project>/<collection>/<name>')
def projects(project, collection, name):
    return '<h1>{}{}{}</h1>'.format(project, collection, name)


# Returns a response object
@app.route('/cookie')
def cookie():
    response = make_response(
        '<h1>This document comes loaded with a cookie</h1>')
    response.set_cookie('answer', '41')
    return response
