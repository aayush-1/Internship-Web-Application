from django.db import models

class PROFESSOR(models.Model):
    First_Name = models.TextField()
    Last_Name = models.TextField()
    Email_ID = models.TextField()
    University = models.TextField()
    Expertise = models.TextField()

class STUDENT(models.Model):
    First_Name = models.TextField()
    Last_Name = models.TextField()
    Email_ID = models.TextField()
    University = models.TextField()
    Branch = models.TextField()
