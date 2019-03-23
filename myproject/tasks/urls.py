from django.urls import path

from . import views

urlpatterns = [path('', views.main_tasks_page, name='main_page'),
               path('<str:option>', views.task_option, name='task_option')]

