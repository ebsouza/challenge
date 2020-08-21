import logging, configparser
from logging.handlers import RotatingFileHandler
from flask import Flask

def greetings():
    print('             ##########################')
    print('             # - ACME - Tasks Robot - #')
    print('             # - v 1.0 - 2020-07-28 - #')
    print('             ##########################')

def initHandler():
    handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    return handler

def initConfig():
    config = configparser.ConfigParser()
    config.read('/tmp/bot/settings/config.ini')
    return config

def initFlaskApp():
    app = Flask(__name__)

    app.logger.addHandler( initHandler() )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123mudar@127.0.0.1:5432/bot_db'

    return app