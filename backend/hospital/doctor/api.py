from doctor.models import Doctor
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DoctorSerializer