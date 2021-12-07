from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=5)
    salary = models.IntegerField(max_length=5)
    joindate= models.DateField()
    class meta:
        db_table = "Employee"
