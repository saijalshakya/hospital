from rest_framework import routers
from .api import DoctorViewSet
from blogs.api import BlogViewSet
from disease.api import DiseaseViewSet
from company.api import CompanyViewSet

router = routers.DefaultRouter()
router.register('api/doctor', DoctorViewSet, 'doctor')
router.register('api/blog', BlogViewSet, 'blog')
router.register('api/disease', DiseaseViewSet, 'disease')
router.register('api/company', CompanyViewSet, 'company-details')

urlpatterns = router.urls