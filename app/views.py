from flask import render_template
from app import app

#Views
@app.route('/')

def index():
    '''
    View root page function that returns the index page and its data

    '''
    title='Home-Welcome to The best news source site online'
    heading='News Sources'
    return render_template('index.html', title=title,heading=heading)

@app.route('/sources/<int:id>')

def articles(id):
    '''
    view root page function to returns the article page and its data
    '''
    return render_template('articles.html', id=id)
