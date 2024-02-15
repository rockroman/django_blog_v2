from django.db import models


# Create your models here.
class Employee(models.Model):
    CHOICES = (
        ("8:00", "8:00AM"),
        ("8:30", "8:30AM"),
        ("9:00", "9:00AM"),
        ("9:30", "9:30AM"),
    )
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_salary = models.IntegerField(null=False, blank=False)
    emp_starting_time = models.TimeField(choices=CHOICES, blank=False, null=False)
    joining_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.emp_name
