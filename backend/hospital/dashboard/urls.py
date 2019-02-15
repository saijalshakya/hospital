from django.urls import path
from . import views
from django.conf.urls import url

app_name = "dashboard"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    url(r'users/$', views.UserView.as_view(), name="users"),
    url(r'users/create$', views.UserCreate.as_view(), name="user-create"),
    
    # # user detail view url dashboard/users/details/n
    # url(r'^users/details/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name="user-detail"),

    # user update view url dashboard/users/n
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name="user-update"),

     # user update view url dashboard/users/n/delete
    url(r'^users/(?P<pk>[0-9]+)/delete$', views.UserDelete.as_view(), name="user-delete")
]