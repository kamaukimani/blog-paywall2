from flask import Flask,request,session
from flask_restful import Api 
from .db import db,migrate 
from .config import Config 
from .models import *
from .routes import *

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    api=Api(app)

    api.add_resource(ClearSession, '/clear', endpoint='clear')
    api.add_resource(IndexArticle, '/articles', endpoint='article_list')
    api.add_resource(ShowArticle, '/articles/<int:id>', endpoint='show_article')
    api.add_resource(Login, '/login', endpoint='login')
    api.add_resource(Logout, '/logout', endpoint='logout')
    api.add_resource(CheckSession, '/check_session', endpoint='check_session')
    api.add_resource(MemberOnlyIndex, '/members_only_articles', endpoint='member_index')
    api.add_resource(MemberOnlyArticle, '/members_only_articles/<int:id>', endpoint='member_article')

    @app.before_request
    def check_if_logged_in():
        open_access_list = [
            'clear',
            'article_list',
            'show_article',
            'login',
            'logout',
            'check_session'
        ]

        if (request.endpoint) not in open_access_list and (not session.get('user_id')):
            return {'error': '401 Unauthorized'}, 401


    return app