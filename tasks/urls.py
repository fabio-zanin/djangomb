from django.urls import path

from . import views

# importa views da aplicação . indica na mesma aplicação "tasks"

urlpatterns = [
    # (urls, views)
    path('helloworld/', views.helloWorld),
    path('', views.tasklist, name = 'tasklist'),
    path('yourname/<str:name>', views.yourname, name = 'yourname' ),
]
