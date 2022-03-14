from django.db import models


class Empolyee1(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    salary = models.IntegerField()
    status = models.BooleanField()
