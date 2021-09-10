from flask import render_template
from app import app
from .request import getSource

#Views
@app.route('/')

def index():
    '''
    View root page function that returns the index page and its data

    '''

    source_business = getSource('business')
    sports_sources = getSource('sports')
    technology_sources = getSource('technology')
    entertainment_sources = getSource('entertainment')

    title='Home-Welcome to The best news source site online'
    heading='News Sources'

    return render_template('index.html', title=title,heading=heading,source_business = source_business,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@app.route('/sources/<int:id>')

def articles(id):
    '''
    view root page function to returns the article page and its data
    '''
    return render_template('articles.html', id=id)
