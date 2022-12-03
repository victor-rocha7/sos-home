from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from accounts.models import Client, Employee
# Create your models here.

class Services(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_date_time = models.DateTimeField()
    value = models.IntegerField(null=True)
    def __str__(self):
        return self.client.id
