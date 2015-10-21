__author__ = 'kiro'
from peewee import *
import datetime
db = PostgresqlDatabase('kiro_db', user='kiro')

class BaseModel(Model):
    class Meta:
        database = db

class Test(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(Test, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

db.connect()
db.drop_tables([Test, Tweet])
#db.create_tables([Test, Tweet])
