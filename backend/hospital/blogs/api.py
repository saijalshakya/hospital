from blogs.models import Blogs
from rest_framework import viewsets, permissions
from .serializers import BlogsSerializers


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.filter(status=1).order_by("-id")
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogsSerializers