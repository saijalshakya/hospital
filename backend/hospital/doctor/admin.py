from django.contrib import admin
from .models import Doctor, Type, Service, Booking, Review


admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Type)
# Register your models here.
