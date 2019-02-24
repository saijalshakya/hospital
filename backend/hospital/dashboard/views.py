from django.shortcuts import render
from players.models import Players, Role
from disease.models import Disease
from blogs.models import Blogs
from company.models import Company
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, View
import _pickle as cPickle
import pickle
from .forms import UserForm, SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.utils.decorators import method_decorator
# Landing page /dashboard
from doctor.models import Doctor,Booking, Service, Type

@login_required(login_url='/admin/accounts/login/')
def IndexView(request):
    return render(request,"dashboard/pages/index.html")



# User Landing page /dashboard/users
class UserView(generic.ListView):
    context_object_name = "users"

    template_name = "dashboard/pages/users/index.html"
   
    def get_queryset(self):
        return User.objects.filter(is_staff=1, is_superuser=0)

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
    model = User
    success_url = reverse_lazy('dashboard:doctors')



# Disease Landing page /dashboard/users
class DiseaseView(generic.ListView):
    context_object_name = "diseases"
    template_name = "dashboard/pages/disease/index.html"
   
    def get_queryset(self):
        return Disease.objects.all()

# Disease Create page /dashboard/users/create
class DiseaseCreate(CreateView):
    model = Disease
    fields = ['name','found','summary','doctor','status','level']

# Disease Update page /dashboard/users
class DiseaseUpdate(UpdateView):
    model = Disease
    fields = ['name',' ','summary','doctor','status', 'level']

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

# Company Details
def CompanyIndex(request):
    company = Company.objects.all()[0]
    return render(request, "dashboard/pages/company/index.html", {"company":company})

# Company Detail Update
def a(request):
    name = request.get("name")
    company = Company.objects.all()
    company.name = name
    company.save()
    return redirect("/admin/company/")


# Disease Update page /dashboard/users
class CompanyDetailUpdate(UpdateView):
    model = Company
    fields = ['name','address','phone1','phone2','email','facebook','instagram','twitter','youtube','fax','pobox']


# class CancerPredictions(generic.ListView):
#     context_object_name = "users"
#     template_name = "dashboard/pages/cancer/index.html"
#     ml = pickle.load(open('/home/saijal/Desktop/model.pkl','rb'))
#     output['oo'] = ml.predict(50,205.40,656.3,545.44,65.500)
#     res = ml
#     def get_queryset(self):
#         return res

class UserFormView(View):
    form_class = UserForm
    template_name = 'dashboard/pages/registration_form.html'

    def get(self, request):
        form  = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form  = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.is_staff = True

            user = User(username=username)
            user.is_staff = True

            user.set_password(password)
            user.save()
            return render(request, "dashboard/pages/doctor/create.html", {'form':form})

        return render(request, self.template_name, {'form':form})


class doctors(generic.ListView):
    context_object_name = "doctors"

    template_name = "dashboard/pages/doctors/index.html"
   
    def get_queryset(self):
        return User.objects.filter(is_staff=1,is_superuser=1)
    

def DoctorCreate(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "dashboard/pages/doctors/create.html")
        
# @login_required(login_url='/admin/accounts/login/')
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect("/admin/doctors")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request, "dashboard/pages/doctors/create.html", context={"form": form})

    form = SignUpForm()
    return render(request, "dashboard/pages/doctors/create.html", {"form": form})


def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect("/admin/users")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request, "dashboard/pages/users/create.html", context={"form": form})

    form = SignUpForm()
    return render(request, "dashboard/pages/users/create.html", {"form": form})


def appointments(request):
    appointment = Booking.objects.order_by("confirm").all()
    return render(request, "dashboard/pages/doctors/appointment/index.html",{"appointment":appointment})

def confirmation(request, id):
    booking = get_object_or_404(Booking, id=id)
    
    if booking.confirm == "0":
        booking.confirm = "1"
        messages.success(request, "Booking is confirmed", extra_tags="1")
    else:
        booking.confirm = "0"
        messages.success(request, "Booking is unconfirmed", extra_tags="0")

    booking.save()
    return redirect("/admin/appointments/")

    
def profile(request):
    pk = request.user.id
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.image = form.cleaned_data['image']
            post.save()
            cat = Type.objects.get(pk=request.POST['type'])
            post.type.add(cat)
            service = Service.objects.get(pk=request.POST['service'])
            post.service.add(service)
            messages.success(request, 'Successfully added')
            return redirect('/profile/')
    else:
        form = ProfileForm()
    args = {'profile': Doctor.objects.filter(user_id=pk).first(), 'form': form}
    return render(request, 'dashboard/pages/doctors/profile.html', args)    


class DocCreate(CreateView):
    model = Doctor
    fields = ['name','image','age','statement','status']


def book(request):
    doctor = Doctor.objects.filter(user_id=request.user.id)[0]
    book = Booking.objects.order_by("-confirm").filter(doctor__id=doctor.id)
    return render(request, "dashboard/pages/doctors/appointment/fordoctor.html",{"appointment":book})


def patientDetails(request, pk):
    booking = Booking.objects.filter(id=pk)[0]
    service = Service.objects.filter(id__in=booking.service)
    return render(request, "dashboard/pages/doctors/appointment/patient.html",{"patient":booking,"service":service})


def checked(request, id):
    booking = get_object_or_404(Booking, id=id)
    
    if booking.checked == "0":
        booking.checked = "1"
        messages.success(request, "Patient is checked", extra_tags="1")
    else:
        booking.checked = "0"
        messages.success(request, "Patient is not checked", extra_tags="0")

    booking.save()
    return redirect("/admin/me-booked/")
