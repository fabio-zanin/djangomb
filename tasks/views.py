from django.http import HttpResponse
from django.shortcuts import render


def helloWorld(request):
    return HttpResponse('Hello World!!')

def tasklist(request):
    return render(request, 'tasks/list.html')

def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name':name})
