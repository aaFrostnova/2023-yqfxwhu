from django.urls import path
from . import views

urlpatterns = [
    # 访问127.0.0.1:8000则会显示views.index
    path('', views.index),
    path('index/', views.index),
    # 访问127.0.0.1:8000则会显示views.graph
    path('graphoverall/', views.graphoverall),
    path('graphofone/', views.graphofone),
    path('search/', views.search),
    path('page1/', views.page1),
    path('page2/',views.page2),
    path('page3/',views.page3)
]