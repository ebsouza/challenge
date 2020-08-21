from flask import Flask, render_template, flash, redirect, url_for
import os
import json

#Config
from config import app_config

#MongoEnfine
from flask_mongoengine import MongoEngine

#Instances
mongoengine = MongoEngine()

def create_app(config_name):

    #Server configs
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    
    mongoengine.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app






