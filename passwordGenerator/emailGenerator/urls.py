from django.urls import path
from emailGenerator import views

urlpatterns = [
    path('', views.home, name='home2'),
    path('result/', views.result, name='email'),
    path('about/', views.about, name='about2'),
]
