from django.db import models

# Create your models here.

class Student(models.Model):

    fullname  = models.CharField(max_length=100)
    level = models.CharField(max_length=25)
    email = models.CharField(max_length=55)
    mobile = models.CharField(max_length=15)

    # Create /Insert / Add -POST
    # Retrive / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE 