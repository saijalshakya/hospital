from django.shortcuts import render
from players.models import Players, Role
from disease.models import Disease,Doctor
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Landing page /dashboard
class IndexView(generic.ListView):
    template_name = "dashboard/pages/index.html"
    def get_queryset(self):
            return ''

# User Landing page /dashboard/users
class UserView(generic.ListView):
    context_object_name = "users"

    template_name = "dashboard/pages/users/index.html"
   
    def get_queryset(self):
        return Players.objects.all()

# # User Detail page /dashboard/users/n
# class UserDetailView(generic.DetailView):
#     model = Players
#     template_name = "dashboard/pages/users/detail.html"

# User Create page /dashboard/users/create
class UserCreate(CreateView):
    model = Players
    fields = ['fn','ln','address','phone','email','password','username','image','role']

# User Update page /dashboard/users
class UserUpdate(UpdateView):
    model = Players
    fields = ['fn','ln','address','phone','email','password','username','image','role']

# User Delete page
class UserDelete(DeleteView):
    model = Players
    success_url = reverse_lazy('dashboard:users')



# Disease Landing page /dashboard/users
class DiseaseView(generic.ListView):
    context_object_name = "diseases"
    template_name = "dashboard/pages/disease/index.html"
   
    def get_queryset(self):
        return Disease.objects.all()

# Disease Create page /dashboard/users/create
class DiseaseCreate(CreateView):
    model = Disease
    fields = ['name','found','summary','doctor']

# Disease Update page /dashboard/users
class DiseaseUpdate(UpdateView):
    model = Disease
    fields = ['name','found','summary','doctor']

# Disease Delete page
class DiseaseDelete(DeleteView):
    model = Disease
    success_url = reverse_lazy('dashboard:diseases')


