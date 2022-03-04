from ast import Str
from re import S
from django.db import models

# Create your models here.

class Feature:
    id : int
    name : Str
    details : str
