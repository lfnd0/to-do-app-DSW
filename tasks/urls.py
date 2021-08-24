from django.urls import path
from .views import TasksListView, TaskCreateView, pendent_tasks, update_task, delete_task, completed_tasks

urlpatterns = [
    path('', TasksListView.as_view(), name='list-tasks'),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('completed-tasks/', completed_tasks, name='completed-tasks'),
    path('pendent-tasks/', pendent_tasks, name='pendent-tasks'),
]
