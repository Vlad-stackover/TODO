from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.index, name='main'),
    path('about', views.about, name='about'),

]