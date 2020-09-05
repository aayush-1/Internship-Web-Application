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
		MyLoginForm = LoginForm(request.POST)

		if MyLoginForm.is_valid():
			prof = PROFESSOR(First_Name = MyLoginForm.cleaned_data['first_name'],Last_Name = MyLoginForm.cleaned_data['last_name'],Email_ID = MyLoginForm.cleaned_data['email'],University = MyLoginForm.cleaned_data['college'],Expertise = MyLoginForm.cleaned_data['expert'], Password = MyLoginForm.cleaned_data['psw'] )
			prof.save();
	return render(request, "home.html")

def home_student(request):
	if request.method == "POST":
	#Get the posted form
		MyLoginForm = LoginForm(request.POST)

		if MyLoginForm.is_valid():
			stud = STUDENT(First_Name = MyLoginForm.cleaned_data['first_name'],Last_Name = MyLoginForm.cleaned_data['last_name'],Email_ID = MyLoginForm.cleaned_data['email'],University = MyLoginForm.cleaned_data['college'],Branch = MyLoginForm.cleaned_data['branch'], Password = MyLoginForm.cleaned_data['psw'] )
			stud.save();
	return render(request, "home.html")

