import os
from dotenv import load_dotenv #allows us to load our environment variables(to fun application)

#establish our base directory. whenever we use "." to reference any location in our app to know we are referncing rangers_shop folder

basedir = os.path.abspath(os.path.dirname(__file__))

#need to establish where our environment varialbes are coming from (this file hidden from github)
load_dotenv(os.path.join(basedir, '.env'))

#create our Config class
class Config():

    """
    Create Config class which will setup our configuration variables.
    Using Environment variables where avaialbe other create config variables.
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anything it needs to be a string'