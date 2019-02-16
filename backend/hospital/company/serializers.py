from rest_framework import serializers
from company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = Company
        