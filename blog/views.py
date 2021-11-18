from django.shortcuts import render
from .models import Persons


def index(request):
    persons = Persons.objects.all()
    return render(request, "index.html", {'persons': persons})
