from django.urls import path
from . import views


urlpatterns = [
    path('<shoesname>/', views.display, name='display')
]