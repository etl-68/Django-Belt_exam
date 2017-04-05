from __future__ import unicode_literals
from ..login_registration.models import User
from django.db import models

# Create your models here.

class Appointment(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, related_name="appointments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
