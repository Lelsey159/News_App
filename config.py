import os

class Config:

    NEWS_API_KEY_URL = 'https://newsapi.org/v2/sources?apiKey=13ced76b35ac4200a34b1ac5b97cae7d'
    NEWS_API_KEY = os.environ.get(13ced76b35ac4200a34b1ac5b97cae7d)

    NEWS_API_SOURCES_URL='http://newsapi.org/v2/top-headlines?''country=us&''apiKey=13ced76b35ac4200a34b1ac5b97cae7d'
    
   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}