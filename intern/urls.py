from django.urls import path

from . import views

urlpatterns = [

    path("<int:pk>/", views.prof_detail, name="prof_detail"),

]