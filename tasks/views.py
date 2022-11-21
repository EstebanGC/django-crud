from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('<h1>Hey, this is a test. Remember you are a bitch!</h1>')
