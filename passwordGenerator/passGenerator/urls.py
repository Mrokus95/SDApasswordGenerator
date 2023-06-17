from django.urls import path
from passGenerator import views

urlpatterns = [
    path('', views.home),
    path("password/", views.password),
]
