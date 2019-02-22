from django.shortcuts import render,get_object_or_404
from disease.models import Disease, Doctor
from blogs.models import Blogs
from django.db.models import Q
from company.models import Company

# Create your views here.

def index(request):
    diseases = Disease.objects.filter(status="1")
    news = Blogs.objects.filter(status="1", types="1")
    events = Blogs.objects.filter(status="1", types="0")
    doctors = Doctor.objects.filter(status="1")
    company = Company.objects.all()
    return render(request, 'front/index.html', {"diseases":diseases,"news":news, "events":events, "doctors":doctors, "company":company})


def search(request):
    doctor = Doctor.objects.filter(name__istartswith=request.POST['name'])[0]
    if doctor:
        return render(request, "front/detail/doctor.html", {'doctor': doctor})
    else:
        return render(request, "front/detail/doctor.html", {'doctor': doctor})


def doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, "front/detail/doctor.html", {'doctor': doctor})


def news(request, pk):
    news = get_object_or_404(Blogs, pk=pk)
    news_more = Blogs.objects.filter(status=1, types=1).exclude(pk=pk)
    return render(request, "front/detail/news.html", {'news': news, 'news_more':news_more})


def events(request, pk):
    events = get_object_or_404(Blogs, pk=pk)
    events_more = Blogs.objects.filter(status=1, types=0).exclude(pk=pk)
    return render(request, "front/detail/events.html", {'events': events, 'events_more':events_more})


def list(request):
    doctor = Doctor.objects.filter(status=1).order_by("-id")
    return render(request, "front/detail/doctorsList.html", {'doctor': doctor})