from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed', views.completed, name='completed'),
    path('remaining', views.remaining, name='remaining'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('detail/<int:task_id>', views.task_detail, name='task_detail'),
]
