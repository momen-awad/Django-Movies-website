from .views import index , todo_list , todo_details,todo_update, todo_delete, todo_details
from django.urls import path
app_name = 'ToDo'
urlpatterns = [
    path('', index, name='todo-index'),
    path('list/', todo_list, name='todo-list'),
    path('details/<int:task_id>/<str:task_name>', todo_details, name='todo-details'),
    path('task/<int:task_id>/update', todo_update, name='todo-update'),
    path('task/<int:task_id>/view', todo_details, name='todo-detail'),
    path('task/<int:task_id>/delete', todo_delete, name='todo-delete')
]