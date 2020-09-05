from django.shortcuts import render
from intern.models import PROFESSOR, STUDENT
from django import forms

def prof_detail(request, pk):

    obj = PROFESSOR.objects.get(pk=pk)

    # car_objs = Car.objects.filter(owner_id=owner_obj.id)

    context = {

        "professors": obj,

        # "drivers": owner_obj,

    }

    return render(request, "prof_detail.html", context)


def portal(request):
    return render(request, "portal.html")

def register_student(request):
    return render(request, "register_student.html")

def register_professor(request):
    return render(request, "register_professor.html")

def login_student(request):
    return render(request, "login_student.html")

def login_professor(request):
    return render(request, "login_professor.html")


def home_professor(request):
	if request.method == "POST":
	#Get the posted form
		# MyLoginForm = LoginForm(request.POST)

		# if MyLoginForm.is_valid():
		prof = PROFESSOR(id = 1,First_Name = request.POST.get('first_name'),Last_Name =  request.POST.get('last_name'),Email_ID =  request.POST.get('email'),University =  request.POST.get('college'),Expertise =  request.POST.get('expert'), Password =  request.POST.get('psw') )
		prof.save();
	return render(request, "home.html")

def home_student(request):
	if request.method == "POST":
	#Get the posted form
		# MyLoginForm = LoginForm(request.POST)

		# if MyLoginForm.is_valid():
		stud = STUDENT(id =1, First_Name =  request.POST.get('first_name'),Last_Name =  request.POST.get('last_name'),Email_ID =  request.POST.get('email'),University =  request.POST.get('college'),Branch =  request.POST.get('branch'), Password =  request.POST.get('psw') )
		stud.save();
	return render(request, "home.html")

