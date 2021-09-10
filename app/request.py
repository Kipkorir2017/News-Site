from app import app
import urllib.request,json
from datetime import datetime
from.models import sources,articles

Source=sources.Source
Article=articles.Article



#Getting api key
api_key=app.config['NEWS_API_KEY']