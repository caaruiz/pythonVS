"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, jsonify
from flask import render_template
from FlaskWebProject1 import app


@app.route('/age',methods=['POST'])
def main():
    content = request.get_json()
    age = content['age']
    name = content['name']
    data = {}
    if age.isdigit() == True:
        age = int(content['age'])
        if age >= 65:
            data= {'name': name, 'message' : 'You are a senior'}
        else:
            data= {'name': name, 'message' : 'You are not a senior'}
    else:
        data= {'name': name, 'message' : 'Age is not a number'}
    return jsonify(data)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
