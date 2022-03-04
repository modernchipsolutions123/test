from collections import Counter
from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('counter/',views.counter, name='counter'),
]