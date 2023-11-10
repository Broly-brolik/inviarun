from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def home(response):
    return render(response, "main/home.html")

def concept(response):
    return render(response, "main/concept.html")

def specialiste(response):
    return render(response, "main/specialiste.html")

def tarif(response):
    return render(response, "main/tarif.html")

def instagram(response):
    return render(response, "main/instagram.html")

def contact(response):
    return render(response, "main/contact.html")