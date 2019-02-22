from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = "front"

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('doctor/<int:pk>/', views.doctor, name='doctor'),
    path('doctor/lists/', views.list, name='list'),
    path('news/<int:pk>/', views.news, name='news'),
    path('events/<int:pk>/', views.events, name='events'),
]