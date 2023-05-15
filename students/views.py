from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView
from .forms import InputForm
from .forms import StudentForm

def list_view(request):
  # dictionary for initial data with
  # field names as keys
  context ={}
  # add the dictionary during initialization
  context["dataset"] = Student.objects.all()
  return render(request, "list_view.html", context)

class StudentCreate(CreateView):
# specify the model for create view
  model = Student
# specify the fields to be displayed
  fields = ['f_name', 'l_name']
 
# Create your views here.
def home_view(request):
  context ={}
  context['form']= InputForm()
  return render(request, "home.html", context)

def home_view2(request):
 form = StudentForm(request.POST or None)
 if form.is_valid():
  form.save()
 # save the form data to model
 
 context ={}
 context['StudentForm']=StudentForm()
 return render(request,"home2.html",context)