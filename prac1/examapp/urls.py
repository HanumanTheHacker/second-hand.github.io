from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.ImageView, name='upload'),
    path('img/', views.Display, name='display')
]