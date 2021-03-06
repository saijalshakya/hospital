from rest_framework import serializers
from disease.models import Disease
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer


class DiseaseSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=True)
    
    class Meta:
        fields = "__all__"
        model = Disease
