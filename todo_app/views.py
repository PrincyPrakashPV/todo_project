from django.shortcuts import render,redirect
from .models import Task
from .forms import Taskform

# Create your views here.


def Task_view(request):
    if request.method == "POST":
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
        s = Task(name=name, priority=priority,date=date)
        s.save()
    obj = Task.objects.all()
    return render(request,'task_view.html',{'obj':obj})

def delete(request,task_id):
    if request.method == "POST":
        ob = Task.objects.get(id=task_id)
        ob.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,task_id):
    t = Task.objects.get(id=task_id)
    form = Taskform(request.POST or None,instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'t':t,'form':form})
