from django.shortcuts import render
from intern.models import PROFESSOR, STUDENT

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

