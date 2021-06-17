from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('home.html', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('contact.html', views.contact, name="contact"),
]
