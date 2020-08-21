import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    MONGODB_SETTINGS = { 'db': 'project', 'host': 'localhost', 'port': 27017 }

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = { 'db': 'test', 'host': 'localhost', 'port': 27017 }

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
