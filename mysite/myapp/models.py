from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):

    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Location = models.CharField(max_length=30)
    Mobile = models.CharField(default=0000000000,max_length=10,unique=True)

    def __str__(self):
        return self.Name
