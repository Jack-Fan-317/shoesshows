from django.shortcuts import render

# Create your views here.
def news(request,num):
    return render(request, 'news'+num+'.html')