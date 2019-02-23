from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = "front"

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('doctor/<int:pk>/', views.doctor, name='doctor'),
    path('disease/<int:pk>/', views.disease, name='disease'),
    path('doctor/book/', views.booking, name='booking'),
    path('doctor/lists/', views.list, name='list'),
    path('news/<int:pk>/', views.news, name='news'),
    path('events/<int:pk>/', views.events, name='events'),
    path('doctor/book/confirm', views.bookingConfirm, name="bookingConfirm"),
    path('doctor/recomment/<int:id>', views.recommend, name="recommend"),
    path("doctor/<int:id>/review",views.review, name="review")
]