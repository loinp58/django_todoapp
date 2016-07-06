from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Todo
from forms import TodoForm

# Create your views here.

def index(request):
	items = Todo.objects.all()
	return render(request, 'todo/index.html', {'items': items})

def create(request):
	form = TodoForm()
	return render(request, 'todo/create.html', {'form': form})

def store(request):
	todoObj = Todo()
	todoObj.name = request.POST.get('name', None)
	todoObj.description = request.POST.get('description', None)
	todoObj.save()
	return HttpResponseRedirect('/')

def destroy(request):
	id = request.POST['id']
	todoObj = Todo.objects.get(pk = id)
	todoObj.delete()
	return HttpResponseRedirect('/')

def edit(request, id):
	todoObj = Todo.objects.get(pk = id)
	form = TodoForm(instance = todoObj)
	return render(request, 'todo/edit.html', {'form': form, 'id': id})

def update(request, id):
	todoObj = Todo.objects.get(pk = id)
	todoObj.name = request.POST.get('name', None)
	todoObj.description = request.POST.get('description', None)
	todoObj.save()
	return HttpResponseRedirect('/')