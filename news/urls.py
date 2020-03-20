from django.urls import path
from . import views


urlpatterns = [
    path('<num>',views.news,name='news'),
]