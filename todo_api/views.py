from todo_api import app
from flask import Blueprint, request

app_route = Blueprint('route', __name__)

@app.route('/')
def index():
    return 'Index'

"""@app.route('/api/users', methods=['GET', 'POST'])
def get_task():
    if request.method == 'GET':
        return f'Got GET-request and arg {request.args}'
    return f'Got {request.method} request'"""

"""@app.route('/api/users/<username>', methods=['GET', 'POST'])
def get_task():
    if request.method == 'POST':
        return f'Got GET-request and arg {request.args}'
    return f'Got {request.method} request'
"""
