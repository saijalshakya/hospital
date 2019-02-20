from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class DoctorView(TemplateView):
    template_name = "doctor/index.html"

    def post(self, request):
        form = DoctorForm(request.POST)
        text = form.cleaned_data['name']