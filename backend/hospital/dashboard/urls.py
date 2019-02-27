from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = "dashboard"

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),


    path('doctor/register/', views.register, name="register"),

    url(r'users/$', views.UserView.as_view(), name="users"),
    # path('cancer/', views.CancerPredictions.as_view(), name="cancer"),
    url(r'users/create$', views.registerUser, name="user-create"),
    
    # # user detail view url dashboard/users/details/n
    # url(r'^users/details/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name="user-detail"),

    # user update view url dashboard/users/n
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name="user-update"),

     # user update view url dashboard/users/n/delete
    url(r'^users/(?P<pk>[0-9]+)/delete$', views.UserDelete.as_view(), name="user-delete"),


    # Disease index view
    url(r'diseases/$', views.DiseaseView.as_view(), name="diseases"),
    url(r'diseases/create$', views.DiseaseCreate.as_view(), name="disease-create"),
    
    # disease update view url dashboard/disease/n
    url(r'^diseases/(?P<pk>[0-9]+)/$', views.DiseaseUpdate.as_view(), name="disease-update"),

     # disease update view url dashboard/disease/n/delete
    url(r'^diseases/(?P<pk>[0-9]+)/delete$', views.DiseaseDelete.as_view(), name="disease-delete"),

    url(r'^diseases/status/(?P<id>[0-9]+)/$', views.DiseaseStatus, name="disease-status"),


    # Blogs index view
    url(r'blogs/$', views.BlogView.as_view(), name="blogs"),
    url(r'blogs/create$', views.BlogCreate.as_view(), name="blog-create"),
    
    # Blogs update view url dashboard/blogs/n
    url(r'^blogs/(?P<pk>[0-9]+)/$', views.BlogUpdate.as_view(), name="blog-update"),

     # Blogs update view url dashboard/blogs/n/delete
    url(r'^blogs/(?P<pk>[0-9]+)/delete$', views.BlogDelete.as_view(), name="blog-delete"),

    url(r'^blogs/status/(?P<id>[0-9]+)/$', views.BlogStatus, name="blog-status"),

    # Blogs index view url dashboard/blogs/n
    url(r'^company/$', views.CompanyIndex, name="company-index"),

    # company view url dashboard/blogs/n
    url(r'^company/update/(?P<pk>[0-9]+)/$', views.CompanyDetailUpdate.as_view(), name="company-update"),


    path('doctors/', views.doctors.as_view(), name="doctors"),
    path('doctors/create-doctors', views.register, name="create-doctors"),

    path('appointments/',views.appointments, name="appointments"),
    path('confirm/<int:id>/', views.confirmation, name="confirm"),
    path('profile/',views.profile, name="profile"),
    path('profile/save/',views.profile,name="profile-save"),
    path('me-booked/',views.book,name="me-booked"),
    path('patient-details/<int:pk>/',views.patientDetails, name="patient-details"),
    path('checked-by-doctor/<int:id>/',views.checked, name="checked"),
    path('patient/submit-report/<int:id>/',views.submitReport, name="submitReport"),
    path('doctors/services/', views.services, name="services"),
    path('doctors/services/status/<int:id>/',views.serviceStatus, name="serviceStatus"),
    path('doctors/services/create/', views.createService, name="create-service"),
    path('doctors/review/', views.review, name="review"),
    path('doctors/review/details/<int:id>/', views.revDetail, name="review-details"),
    path("doctors/review/status/<int:id>/",views.reviewStatus, name="review-status"),
    path("doctors/review/delete/<int:id>/", views.reviewDelete, name="review-delete")

]