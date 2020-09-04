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