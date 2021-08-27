from django.urls import path
from .views import TasksListView, TaskCreateView, update_description_task, update_status_task, delete_task, completed_tasks, pendent_tasks

urlpatterns = [
    path('', TasksListView.as_view(), name='list-tasks'),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),
    path('update-description-task/<int:id>',
         update_description_task, name='update-description-task'),
    path('update-status-task/<int:id>/',
         update_status_task, name='update-status-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('completed-tasks/', completed_tasks, name='completed-tasks'),
    path('pendent-tasks/', pendent_tasks, name='pendent-tasks'),
]
