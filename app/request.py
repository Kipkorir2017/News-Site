from app import app
import urllib.request,json
from datetime import datetime
from.models import sources,articles

Source=sources.Source
Article=articles.Article



#Getting api key
api_key=app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_SOURCES_BASE_URL']
article_url = app.config['ARTICLES_BASE_URL']


def getSource(category):
    '''
    Function that gets the json response to url request
    '''
    getSource_url=base_url.format(category,api_key)

    with urllib.request.urlopen(getSource_url) as url:
        getSource_data=url.read()
        getSource_response=json.loads(getSource_data)

        sources_results=None

        if getSource_response['sources']:
            sources_results_list=getSource_response['sources']
            sources_results=sources_results = process_sources(sources_results_list)

    return sources_results

# def process_sources(sources_list):