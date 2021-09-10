from flask import render_template
from app import app

#Views
@app.route('/')

def index():
    '''
    View root page function that returns the index page and its data

    '''
    title='Home-Welcome to The best news source site online'

    return render_template('index.html')