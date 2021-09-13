
import urllib.request,json
from .models import Sources,Articles
from datetime import datetime

#Getting api key
api_key=None


# Getting the movie base url
base_url = None
article_url =None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    article_url=app.config['ARTICLES_BASE_URL']


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
            sources_results=sources_results = process_results(sources_results_list)

    return sources_results

def process_results(source_list):
    '''
    Function that processes the source results and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns:
        sources_results: A list of sources objects

    '''
    sources_results=[]
    for sources_item in source_list:
        id=sources_item.get('id')
        name = sources_item.get('name') 
        description=sources_item.get('description')
        url=sources_item.get('url')
        category=sources_item.get('category') 
        country=sources_item.get('country')

        sources_objects= Sources(id, name, description, url, category, country)
        sources_results.append(sources_objects)

    return sources_results

def get_articles(id):
    '''
    Function that returns the articles objects

    '''
    get_article_url=article_url.format(id,api_key)
    with urllib.request.urlopen(get_article_url)as url:
        get_article_data=url.read()
        get_article_response=json.loads(get_article_data)

        articles_object = None
        if get_article_response['articles']:
            get_source_article=get_article_response['articles']
            articles_object = process_articles(get_source_article)

    return articles_object 



def process_articles(articles_list):
        '''
        Function that processes the articles results and transform them to a list of Objects

        Args:
            article_list: A list of dictionaries that contain sources details

        Returns:
            article_results: A list of sources objects
        '''
        articles_object = []
        for article_item in articles_list:
            id = article_item.get('id')
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            publishedAt = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
            date = publishedAt.strftime('%d.%m.%Y')
		
        
            articles_result = Articles(id, author, title, description, url, urlToImage,date)
            articles_object.append(articles_result)

        return articles_object
