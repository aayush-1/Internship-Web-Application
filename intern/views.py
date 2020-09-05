from django.shortcuts import render
from intern.models import PROFESSOR, STUDENT
from django import forms

X=1
Y=1
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
		prof = PROFESSOR(id = X,First_Name = request.POST.get('first_name'),Last_Name =  request.POST.get('last_name'),Email_ID =  request.POST.get('email'),University =  request.POST.get('college'),Expertise =  request.POST.get('expert'), Password =  request.POST.get('psw') )
		prof.save();
		X+=1
	return render(request, "home.html")

def home_student(request):	
	if request.method == "POST":
		stud = STUDENT(id =Y, First_Name =  request.POST.get('first_name'),Last_Name =  request.POST.get('last_name'),Email_ID =  request.POST.get('email'),University =  request.POST.get('college'),Branch =  request.POST.get('branch'), Password =  request.POST.get('psw') )
		stud.save();
		Y+=1
	return render(request, "home.html")

def home(request):
	# data = []
	if request.method == "POST":
		data = PROFESSOR.objects.filter(First_Name = request.POST.get("first_name"))

	return render(request, "home.html",{"data" : data})

