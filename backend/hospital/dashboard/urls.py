from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.users, name="users"),
    path('users/add',views.addUsers, name="addUsers")
]