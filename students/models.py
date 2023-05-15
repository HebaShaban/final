from django.db import models

# Create your models here.
class Student(models.Model):
 f_name = models.CharField(max_length=255)
 l_name = models.CharField(max_length=255)
 mobile = models.IntegerField()
 birth_date = models.DateField()
 
 def __str__(self):
   return f"{self.f_name} {self.l_name}"
