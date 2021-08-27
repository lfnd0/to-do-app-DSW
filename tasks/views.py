from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils import timezone
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


def update_description_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskModelForm(instance=task)

    if(request.method == 'POST'):
        form = TaskModelForm(request.POST, instance=task)
        if(form.is_valid()):
            task.status = 'Pendente'
            task.creation_date = timezone.now()
            task.save()
            return redirect('list-tasks')
        else:
            return render(request, 'tasks/update-description-task.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/update-description-task.html', {'form': form, 'task': task})


def update_status_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if(task.status == 'Pendente'):
        task.status = 'Concluída'
        task.creation_date = timezone.now()
        task.save()

    return redirect('list-tasks')


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('list-tasks')


def completed_tasks(request):
    tasks = Task.objects.filter(status='Concluída')
    return render(request, 'tasks/completed-tasks.html', {'tasks': tasks})


def pendent_tasks(request):
    tasks = Task.objects.filter(status='Pendente')
    return render(request, 'tasks/pendent-tasks.html', {'tasks': tasks})
