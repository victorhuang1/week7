import os
import json
from random import randint
from faker import Faker
from simpledu.models import db,User,Course,Chapter

fake=Faker()
def iter_users():
    yield User(
            username='Jace Ma',
            email='jackma@example.com',
            password='zxcvbnm',
            job='研发工程狮子',
            )
def iter_courses():
    author=User.query.filter_by(username='Jace Ma').first()
    with open(os.path.join(os.path.dirname(__file__),'..','datas','courses.json')) as f:
        courses=json.load(f)
    for course in courses:
        yield Course(
            name=course['name'],
            description=course['description'],
            image_url=course['image_url'],
            author=author
            )
def iter_chapters():
    for course in Course.query:
        for i in range(randint(3,10)):
            yield Chapter(
                name=fake.sentence(),
                course=course,
                video_url='https://labfile.oss.aliyuncs.com/courses/923/week2_mp4/2-1-1-mac.mp4',
                video_duration='{}:{}'.format(randint(10,30),randint(10,59))
                )
def run():
    for user in iter_users():
        db.session.add(user)
        db.session.commit()
    for course in iter_courses():
        db.session.add(course)
        db.session.commit()
    for chapter in iter_chapters():
        db.session.add(chapter)
        db.session.commit()
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
