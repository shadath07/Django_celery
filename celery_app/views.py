from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
from .services import *

# Create your views here.


def index(request):
    send_mail_task.delay()
    return HttpResponse("<h1>Hello, From Celery </h1>")