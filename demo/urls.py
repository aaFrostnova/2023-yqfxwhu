from django.urls import path
from . import views

urlpatterns = [
    path('demo/<int:num>/', views.hello),
    path('demo/index/', views.index),
    path('demo/graph/', views.graph),
]