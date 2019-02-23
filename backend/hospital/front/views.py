from django.shortcuts import render,get_object_or_404
from disease.models import Disease, Doctor
from doctor.models import Service, Doctor, Booking, Type, Review
from blogs.models import Blogs
from django.db.models import Q
from company.models import Company
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect




def index(request):
    diseases = Disease.objects.filter(status="1")
    news = Blogs.objects.filter(status="1", types="1")
    events = Blogs.objects.filter(status="1", types="0")
    doctors = Doctor.objects.filter(status="1")
    company = Company.objects.all()
    t = Type.objects.order_by("-counter").all()[0]
    return render(request, 'front/index.html', {"t":t,"diseases":diseases,"news":news, "events":events, "doctors":doctors, "company":company})

def recommend(request, id):
    doctor = Doctor.objects.filter(type__id=id)
    return render(request, "front/detail/doctorsList.html", {"doctor":doctor})


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


def disease(request, pk):
    disease = Disease.objects.get(pk=pk)
    disease_name = disease.name
    blogs = Blogs.objects.filter(title__istartswith=disease_name)
    return render(request, "front/detail/disease.html", {"disease":disease,"blogs":blogs})
    
    
def booking(request):
    date = request.POST["dated"]
    time = request.POST["timed"]
    dr = Doctor.objects.filter(pk=request.POST["doctor"])[0]
    services = Service.objects.filter(pk__in=request.POST.getlist('visit'))
    total=0
    for i in services:
        total+=int(i.price)
    return render(request, "front/booking/booking.html", {"date":date, "time": time,"total":total, "dr":dr,"services":services})


def bookingConfirm(request):
    fn = request.POST['fn']
    ln = request.POST['ln']
    email = request.POST['email']
    phone = request.POST['phone']
    location = request.POST['location']
    street1  = request.POST['street1']
    street2  = request.POST['street2']
    services = request.POST.getlist('service')
    dr = request.POST['doctor']
    city  = request.POST['city']
    state  = request.POST['state']
    postal  = request.POST['postal']


    book = Booking.objects.create(service=services,fn=fn,ln=ln,email=email,phone=phone,location=location,street1=street1,street2=street2,city=city, state=state, postal=postal)
    book.save()

    doc = Doctor.objects.get(pk=dr)
    a= doc.type.all()[0]
    t = Type.objects.filter(id=a.id)[0]
    t.counter = str(int(t.counter)+1)
    t.save()
    book.doctor.add(doc)
    return render(request,"front/booking/confirm.html",{"a":t})


def review(request, id):
    if request.method == 'POST':
        rate = request.POST.get('rate')
        title = request.POST['title']
        re = request.POST['re']
        doc = Doctor.objects.filter(id=id)[0]
        review = Review.objects.create(rate=rate,title=title,rev=re)
        review.save()
        review.doctor.add(doc)
        messages.success(request, "Review send. It will be published once the doctor accepts it.")
        return HttpResponseRedirect('/doctor/%d' % int(id))
    else:
        doctor = Doctor.objects.filter(id=id)[0]
        return render(request, "front/detail/review.html", {"doctor":doctor})    
