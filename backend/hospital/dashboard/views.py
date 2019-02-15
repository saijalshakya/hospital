from django.shortcuts import render
from players.models import Players, Role
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


class IndexView(generic.ListView):
    template_name = "dashboard/pages/index.html"
    def get_queryset(self):
            return ''

class UserView(generic.ListView):
    context_object_name = "users"

    template_name = "dashboard/pages/users/index.html"
   
    def get_queryset(self):
        return Players.objects.all()

class UserCreateView(generic.CreateView):
    pass

class create(CreateView):
    model = Players
    fields = ['fn','ln','address','phone','email','password','username','image','role']

def addUsers(request):
    if request.method == 'POST':
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        image = request.POST.get("image")
        user = Players.objects.create(fn=fn,ln=ln,address=address,phone=phone,email=email,password=password,username=username,image=image)
        return render(request, "dashboard/pages/users/a.html",{"a":a})
    else:
        roles = Role.objects.all()
        return render(request, "dashboard/pages/users/create.html", context={"roles":roles})


class UserCreate(CreateView):
    model = Players
    fields = ['fn','ln','address','phone','image']