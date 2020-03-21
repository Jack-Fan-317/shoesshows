from django.urls import path
from . import views


urlpatterns = [
    path('<shoesname>', views.display, name='display'),
    path('<shoesname>/<more_shoesname>', views.load_more, name='shoes_more'),
    path('<shoesname>/<more_shoesname>', views.load_more, name='shoes_more'),
]