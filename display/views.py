from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request, shoesname):
    return render(request, shoesname+'.html')


def load_more(request, shoesname, more_shoesname):
    return render(request, more_shoesname+'.html')