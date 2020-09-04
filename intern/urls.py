from django.urls import path

from . import views

urlpatterns = [

	path("portal/", views.portal, name="portal"),
	path("login_student/", views.login_student, name="login_student"),
	path("login_professor/", views.login_professor, name="login_professor"),
	path("register_student/", views.login_student, name="register_student"),
	path("register_professor/", views.login_professor, name="register_professor"),
	# path("registration/", views.registration_student, name="registration"),
    path("<int:pk>/", views.prof_detail, name="prof_detail"),

]