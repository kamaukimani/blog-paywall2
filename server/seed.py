#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import create_app
from app.db import db
from app.models import Article, User


fake = Faker()

app=create_app()

with app.app_context():

    print("Deleting all records...")
    Article.query.delete()
    User.query.delete()

    fake = Faker()

    print("Creating users...")
    users = []
    usernames = []
    for i in range(25):

        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        
        usernames.append(username)

        user = User(username=username)
        users.append(user)

    db.session.add_all(users)

    print("Creating articles...")
    articles = []

    for user in users:
        for i in range(randint(1,5)):
            content = fake.paragraph(nb_sentences=8)
            preview = content[:25] + '...'
            
            article = Article(
                author=fake.name(),
                title=fake.sentence(),
                content=content,
                preview=preview,
                minutes_to_read=randint(1,20),
                is_member_only = rc([True, False, False]),
                user=user,
            )

            articles.append(article)
    
        

    db.session.add_all(articles)
    
    db.session.commit()
    print("Complete.")