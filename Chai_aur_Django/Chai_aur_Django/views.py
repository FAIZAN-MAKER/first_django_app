from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to Chai aur Django!")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is the about page of Chai aur Django.")

def contact(request):
    return HttpResponse("Contact us at contact@example.com")