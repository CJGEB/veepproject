from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               path('<int:item_nbr>', views.detail, name='detail'),
                ]
