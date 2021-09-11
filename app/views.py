from flask import render_template
from app import app
from .request import getSource,get_articles

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
    general_sources=getSource('general')

    title='Home-Welcome to The best news sources site online'
    heading='News Sources'

    return render_template('index.html', title=title,heading=heading,general_sources=general_sources,source_business = source_business,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@app.route('/sources/<id>')

def articles(id):
    '''
    view root page function to returns the article page and its data
    '''
    
    source_articles = get_articles(id)
    # title = f'{articles.title}'

    return render_template('articles.html', id=id,source_articles=source_articles)
