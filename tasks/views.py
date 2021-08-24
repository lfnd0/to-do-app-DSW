from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render

from tasks.models import Task
from tasks.forms import TaskModelForm


class TasksListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list-tasks.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'tasks/create-task.html'
    success_url = reverse_lazy('list-tasks')


def update_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.status = 'Concluída'
    task.save()
    return redirect('list-tasks')


def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('list-tasks')


def completed_tasks(request):
    tasks = Task.objects.filter(status='Concluída')
    return render(request, 'tasks/completed-tasks.html', {'tasks': tasks})


def pendent_tasks(request):
    tasks = Task.objects.filter(status='Pendente')
    return render(request, 'tasks/pendent-tasks.html', {'tasks': tasks})
