from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re
import datetime

# Create your views here.
def start(request):
    return render(request, 'login_registration/start.html')

def actions(request):
    error = False
    print 'cool beans'
    if request.method == 'POST':
        if request.POST['action'] == 'register':
            #name
            name = User.objects.name_validate(request.POST['name'])
            if not name:
                messages.add_message(request, messages.ERROR, 'Name too short!', extra_tags = 'name')
                error = True
            #email
            email = User.objects.email_validate(request.POST['email'])
            if not email:
                messages.add_message(request, messages.ERROR, 'Invalid email!', extra_tags = 'email')
                error = True
            #check if email exists
            email_exists = User.objects.email_exists(request.POST['email'])
            if not email_exists:
                messages.add_message(request, messages.ERROR, 'Email already exists!', extra_tags = 'email')
                error = True
            #password
            password = User.objects.password_validate(request.POST['password'])
            if not password:
                messages.add_message(request, messages.ERROR, 'Password too short!', extra_tags = 'password')
                error = True
            #confirm that the passwords match
            password_match = User.objects.password_match(request.POST['password'], request.POST['confirm_password'])
            if not password_match:
                messages.add_message(request, messages.ERROR, 'Passwords do not match!', extra_tags = 'match')
                error = True
            #confirm that dob is valid

            if error:
                print messages
                return redirect('/')
            else:
                new = User.objects.createUser(name = request.POST['name'], email = request.POST['email'],password = request.POST['password'], dob = request.POST['dob'])
                request.session['user_id']=new.id
                request.session['user_name']=new.name
                request.session['user_email']=new.email
                request.session['user_dob']=str(new.dob)
                return redirect('appointments:start')

        elif request.POST['action'] == 'login':
            try:
                user = User.objects.get(email = request.POST['email'])
            except Exception:
                messages.add_message(request, messages.ERROR, 'Email does not exist. Please register to login in!', extra_tags = 'deny')
                return redirect('/')

            if not User.objects.passwordsMatchCheck(request.POST['password'], user.password):
                messages.add_message(request, messages.ERROR, 'Email or password is not correct!', extra_tags = 'deny')
                return redirect('login_registration:start')
            else:
                request.session['user_id']=user.id
                request.session['user_name']=user.name
                request.session['user_email']=user.email
                request.session['user_dob']=str(user.dob)
                return redirect('appointments:start')
