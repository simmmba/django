from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('index/', views.index),
    path('<int:no>/detail/', views.detail),
]