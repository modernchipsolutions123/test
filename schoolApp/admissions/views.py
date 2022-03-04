from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def addAddmissions(request):
    return HttpResponse('<h2>This is add addmission view</h2> <h1>Welcome To My eSchool App</h1>')

def addmissionsReport(request):
    return HttpResponse('<h1>This is addmission report view</h1>')

def home(request):
    return HttpResponse('Welcome to Django')

def ram(request):
    contact = {'yuvi':964280}
    return render(request,'ram.html',{'contact':contact})