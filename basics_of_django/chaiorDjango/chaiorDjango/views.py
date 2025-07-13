from django.http import HttpResponse
from django.shortcuts import render

def home(requests):
    # return HttpResponse("hello you are at rajat world and learning Django at chai and code")
    return render(requests,'index.html')

def about(requests):
    return HttpResponse("hello user this is your about page")

def contact(requests):
    return HttpResponse(" <h1> hello user this is yoyr contact page </h1>")

