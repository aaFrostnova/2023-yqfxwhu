from django.urls import path
from . import views

urlpatterns = [
    # 访问127.0.0.1:8000则会显示views.index
    path('', views.index),
    # 访问127.0.0.1:8000则会显示views.graph
    path('graph/', views.graph),
]