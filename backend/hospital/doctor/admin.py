from django.contrib import admin
from .models import Doctor, Type, Service


admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Type)
# Register your models here.
