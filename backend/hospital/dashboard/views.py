from django.shortcuts import render
from players.models import Players, Role
from disease.models import Disease,Doctor
from blogs.models import Blogs
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages


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
    fields = ['name','found','summary','doctor','status']

# Disease Update page /dashboard/users
class DiseaseUpdate(UpdateView):
    model = Disease
    fields = ['name','found','summary','doctor','status']

# Disease Delete page
class DiseaseDelete(DeleteView):
    model = Disease
    success_url = reverse_lazy('dashboard:diseases')


def DiseaseStatus(request, id):
    disease = get_object_or_404(Disease, id=id)
    status = disease.status
    
    if(status == "1"):
        disease.status = "0"
        messages.success(request, "Status unpublished successfully.", extra_tags="0")
    else:
        disease.status = "1"
        messages.success(request, "Status published successfully.", extra_tags="1")

    disease.save()
    return redirect("/admin/diseases/")



# Blogs Landing page /dashboard/users
class BlogView(generic.ListView):
    context_object_name = "blogs"
    template_name = "dashboard/pages/blogs/index.html"
   
    def get_queryset(self):
        return Blogs.objects.all()

# Blogs Create page /dashboard/users/create
class BlogCreate(CreateView):
    model = Blogs
    fields = ['title','intro','description','image','status']

# Blogs Update page /dashboard/users
class BlogUpdate(UpdateView):
    model = Blogs
    fields = ['title','intro','description','image','status']

# Blogs Delete page
class BlogDelete(DeleteView):
    model = Blogs
    success_url = reverse_lazy('dashboard:blogs')

def BlogStatus(request, id):
    blog = get_object_or_404(Blogs, id=id)
    status = blog.status
    
    if(status == "1"):
        blog.status = "0"
        messages.success(request, "Status unpublished successfully.", extra_tags="0")
    else:
        blog.status = "1"
        messages.success(request, "Status published successfully.", extra_tags="1")

    blog.save()
    return redirect("/admin/blogs/")