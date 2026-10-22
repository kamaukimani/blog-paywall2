from flask import Flask 
from flask_restful import Api 
from .db import db,Migrate 
from .config import Config 

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(db,app)


    return app