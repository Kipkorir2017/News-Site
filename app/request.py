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

        if getSource_response['results']:
            sources_results_list=getSource_response['results']
            sources_results=sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function that processes the source results and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns:
        sources_results: A list of sources objects

    '''
    sources_results=[]
    for sources_item in sources_list:
        id=sources_item.get('id')
        name = sources_item.get('name') 
        description=sources_item.get('description')
        url=sources_item.get('url')
        category=sources_item.get('category') 
        country=sources_item.get('country')

        sources_objects= Source(id, name, description, url, category, country)
        sources_results.append(sources_objects)
        
    return sources_results