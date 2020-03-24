from django.urls import path
from . import views


urlpatterns = [
    path('<brand>', views.shoes_list, name='shoes_list'),
    path('<brand>/<series>/<shoesname>', views.shoes_detail, name='shoes_detail'),
    path('<brand>/<brand_more>', views.brand_more, name='brand_more'),
]