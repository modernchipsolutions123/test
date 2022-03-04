from django.shortcuts import render
# from django.http import HttpResponse

from .models import TodoItem

# Create your views here.

def todo_view(request):
    all_todo_items = TodoItem.objects.all() 
    return render(request,'todo_app/todo.html',{'all_items':all_todo_items})
 



