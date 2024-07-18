from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html',{
        'tasks':tasks,
    })


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


# def add_task(request):
#     if request.method == 'POST':
#         task_name = request.POST.get('task_name')
#         task_description = request.POST.get('task_description')
#         due_date = request.POST.get('due_date')
#         due_time = request.POST.get('due_time')
#     return render(request, 'add_task.html')


def completed(request):
    completed_tasks = Task.objects.filter(completed=True) 
    return render(request, 'completed.html',{
        'tasks':completed_tasks,
    })

def delete_task(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    return render(request, 'delete.html', {'task': tasks})

def remaining(request):
    remaining_tasks = Task.objects.filter(completed=False) 
    return render(request, 'remaining.html',{
        'tasks':remaining_tasks,
    }
    )

def task_detail(request, task_id):
    task_det = get_object_or_404(Task,id=task_id)
    return render(request, 'task_detail.html', {'task': task_det})