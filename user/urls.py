from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('publish/', views.publish, name="publish"),
    path('publish_list/', views.publish_list, name="publish_list"),
]
