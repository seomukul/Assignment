from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # No longer `editable=False`
    designation = models.CharField(max_length=100)  # No longer `editable=False`
    short_description = models.TextField()
    
    def __str__(self):
        return self.name
