from __future__ import unicode_literals
from django.db import models
import re
import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

class UserManager(models.Manager):
    #Check first name
    def name_validate(self, name):
        if len(name) > 1:
            return True
        else:
            return False
    #Check email length
    def email_validate(self, email):
        if not EMAIL_REGEX.match(email):
            return False
        else:
            return True
    #Check if email already exists
    def email_exists(self, email):
        check = User.objects.filter(email = email).exists()
        if check:
            return False
        else:
            return True
    #Check password
    def password_validate(self, password):
        if len(password) > 5:
            return True
        else:
            return False
    #Check password
    def password_match(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False
    #Create User
    def createUser(self, name, email, password, dob):
        user = self.create(name= name, email = email, password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()), dob = dob)
        return user
    #Check entered password matches database password
    def passwordsMatchCheck(self, entered_pw, db_pw):
        if bcrypt.hashpw(entered_pw.encode(), db_pw.encode()) != db_pw:
            return False
        else:
            return True

class User(models.Model):
    name = models.TextField(max_length = 50)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
