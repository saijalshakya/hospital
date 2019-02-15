from django.urls import path
from . import views
from django.conf.urls import url

app_name = "dashboard"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    url(r'users/$', views.UserView.as_view(), name="users"),
    url(r'users/create$', views.UserCreate.as_view(), name="user-create"),
    
]