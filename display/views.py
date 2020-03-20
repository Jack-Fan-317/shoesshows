from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request, shoesname):
    return render(request, shoesname+'.html')