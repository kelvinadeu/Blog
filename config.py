import os
class Config:

    '''
    General configuration parent class

    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')

    BASE_URL='http://quotes.stormconsultancy.co.uk/{}.json'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1234localhost/kevblog'


    DEBUG = True

class ProdConfig(Config):

    pass

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''



class DevConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''




config_options = {
'development':DevConfig,
'production':ProdConfig
}
