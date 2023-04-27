from django.urls import path, re_path
from menu import views

urlpatterns = [
    re_path(r'^', views.menu, name='menu'),
    re_path(r'^(\d+)', views.menu, name='menu'),
]