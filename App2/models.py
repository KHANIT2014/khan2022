from django.db import models


# Create your models here.
class Empolyee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    salary = models.IntegerField()
    status = models.BooleanField()
