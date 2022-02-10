from django.db import models

# Create your models here.


class Emp(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=10)
