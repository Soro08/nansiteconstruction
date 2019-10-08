from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='bootcamp'),
    path('save',views.save_info,name='bootcamp_etudiant_save'),
]