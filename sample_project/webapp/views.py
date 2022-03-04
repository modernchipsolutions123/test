from django.shortcuts import render
from django.http import HttpResponse  


# Create your views here.


def display(request):
    return HttpResponse('<h1> hello welcome to django </h1>')



def name(request,name):
    return HttpResponse(f'hello my name is {name}')


def details(request):
    data ={'name':'sai', 'age':25, 'location':'banglure'}
    return HttpResponse (f"my name is <h1>{data['name']}</h1> age is <h1>{data['age']}</h1> and location is <h1>{data['location']}</h1>") 




def stu_dis(request,name,age):
    return HttpResponse(f'hello my name is {name} age is {age}')


def emp_det(request,emp_id,emp_name):
    data = {'emp_id':emp_id, 'emp_name':emp_name}
    return render(request,'webapp/index.html',{'data':data})

def add(request):
    a,b = 10,20
    c =a + b
    return HttpResponse(f'sum of a and b is ,{c}')
