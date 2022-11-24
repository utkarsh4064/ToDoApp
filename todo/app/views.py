from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks= Task.objects.all()
    form= TaskForm()
    if(request.method=='POST'):
        form= TaskForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('/')
    dict= {'tasks': tasks, 'form': form}
    return render(request, 'index.html', dict)

def update(request, pk):
    task= Task.objects.get(id=pk)
    form= TaskForm(instance= task)
    dict= {'form': form}
    if(request.method=="POST"):
       form= TaskForm(request.POST, instance= task) 
       if form.is_valid():
        form.save()
       return redirect('/')
    

    return render(request, 'update.html', dict)

def delete(request, pk):
    task= Task.objects.get(id=pk)
    if request.method== 'POST':
       task.delete()
       return redirect("/")
    dict= {'task': task}

    return render(request, 'delete.html', dict)