from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview, name='home'),
    path('about', views.aboutpageview, name='aboutpageview'),
    path('contact', views.contactpageview, name='contactpageview'),
    path('portfolio', views.portfoliopageview, name='portfoliopageview'),
]
