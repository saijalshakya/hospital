from disease.models import Disease
from rest_framework import viewsets, permissions
from .serializers import DiseaseSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.filter(status=1).order_by("-id")
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DiseaseSerializer

    # # # queryset = Blogpost.objects.all().order_by('date')
    # # serializer_class = serializers.BlogpostSerializer

    # def get_queryset(self):
    #     # Chances are, you're doing something more advanced here 
    #     # like filtering.
    #     Disease.objects.all().order_by('-id')

    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, *args, **kwargs)
    #     qs = self.get_queryset()
    #     all_doctors = Doctor.objects.filter(
    #         id__in=Disease.doctor.through.objects.filter(
    #             disease__in=qs
    #         ).values('doctor_id')
    #     )
    #     doctor_names = {}
    #     for dr in all_doctors:
    #         doctor_names[dr.id] = dr.name

    #     doctors_map = defaultdict(list)
    #     for m2m in Disease.doctor.through.objects.filter(disease__in=qs):
    #         doctors_map[m2m.disease_id].append(
    #             doctor_names[m2m.doctor]
    #         )

    #     for a in response.data:
    #         a['doctor'] = doctors_map.get(a['id'], [])

    #     return response
