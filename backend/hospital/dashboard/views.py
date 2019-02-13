from django.shortcuts import render
from players.models import Players

# Create your views here.


def index(request):
    return render(request, "dashboard/pages/index.html")

def users(request):
    users = Players.objects.order_by("-id").all()
    return render(request, "dashboard/pages/users/index.html", context={"users":users})