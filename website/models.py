from django.db import models
from mongoengine import *
from pymatgen import Structure


# Create your models here.
# connect('students', host='127.0.0.1', port=27017)


class Student(Document):
    name = StringField(max_length=16)
    age = IntField(default=-1)
    sex = StringField








