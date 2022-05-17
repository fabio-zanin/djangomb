from django.urls import path

from . import views

# importa views da aplicação . indica na mesma aplicação "tasks"

urlpatterns = [
    path('helloworld/', views.helloWorld),
    # (urls, views)
]
