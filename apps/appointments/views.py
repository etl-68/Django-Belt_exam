from django.shortcuts import render, redirect
from .models import Appointment
from ..login_registration.models import User
import datetime
# Create your views here.

def start(request):
    appointments = Appointment.objects.all()
    context={
        'appointments': appointments,
        'today': datetime.date.today(),
        'time': datetime.datetime.now().strftime('%H:%M:%p'),
    }
    return render(request, 'appointments/start.html', context)

def new(request):
    if request.method=='POST':
        if request.POST['new'] == 'new':
            user = User.objects.get(id=request.session['user_id'])
            new = Appointment.objects.create(task=request.POST['task'], date=request.POST['date'], time=request.POST['time'], user=user)
            return redirect('appointments:start')

def edit(request, id):
    appointment = Appointment.objects.get(id=id)
    context={
        'appointment': appointment
    }
    return render(request, 'appointments/edit.html', context)

def delete(request, id):
    delete = Appointment.objects.get(id=id).delete()
    return redirect('appointments:start')

def change(request, id):
    if request.method=='POST':
        if request.POST['update'] == 'update':
            changeAppointment.objects.get(id=id).update(task=request.POST['task'])
            return redirect('appointments:start')
