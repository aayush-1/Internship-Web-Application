from django.urls import path

from . import views

urlpatterns = [

	path("portal/", views.portal, name="portal"),
	path("login_student/", views.login_student, name="login_student"),
	path("login_professor/", views.login_professor, name="login_professor"),
	path("register_student/", views.register_student, name="register_student"),
	path("register_professor/", views.register_professor, name="register_professor"),
	path("home_professor/", views.home_professor, name="home_professor"),
	path("home_student/", views.home_student, name="home_student"),
    path("<int:pk>/", views.prof_detail, name="prof_detail"),

]