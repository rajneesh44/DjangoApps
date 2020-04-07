from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItems

def todoView(request):
    allitems = TodoItems.objects.all()
    return render(request, 'todo.html', {'allitems': allitems})
# Create your views here.

def addTodo(request):
    #create a new todo #save #redirect
    new_item = TodoItems(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo')