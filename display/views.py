from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shoes_list(request, brand):
    return render(request, brand+'.html')


def shoes_detail(request, brand, series, shoesname):
    return render(request, shoesname+'.html')


def brand_more(request, brand, brand_more):
    return render(request, brand_more+'.html')