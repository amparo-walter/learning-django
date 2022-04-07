from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles_view),
    path('articles/create', views.articles_create_view),
]