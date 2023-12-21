from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('news/<str:category>/', views.news_by_category, name='news_by_category'),

]