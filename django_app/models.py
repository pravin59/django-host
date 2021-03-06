from django.db import models

# Create your models here.

class Employee(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length= 25)
  mobile = models.CharField(max_length=15)
  email = models.EmailField()

  def __str__(self):
    return self.first_name
