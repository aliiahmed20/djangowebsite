from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from . models import Product



def index(request):
    products = Product.objects.all()
    return render(request, "home.html", {'products': products})

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    return render(request, "project.html")
