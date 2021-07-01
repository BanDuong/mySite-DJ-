from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import LaviType

# Create your views here.
def index(request):
    return render(request,"laviApp/index.html",{})

def home(request):
    return render(request,"laviApp/home.html",{})

class getList(generic.ListView):
    queryset = LaviType.objects.all().order_by("created_at")
    template_name = "laviApp/list.html"
    context_object_name = "list"
    paginate_by = 2

class getDetail(generic.DetailView):
    pass

