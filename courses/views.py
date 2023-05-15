from django.shortcuts import render
from .models import course
# Create your views here.
def list2_view(request):
# dictionary for initial data with
# field names as keys
 context ={}
# add the dictionary during initialization
 context["dataset"] = course.objects.all()

 return render(request, "list2_view.html", context)