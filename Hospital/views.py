import re
import random

from django.contrib import messages
from email_validator import validate_email, EmailNotValidError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import auth
from .forms import (AddUserForm)
from .models import UserDetails,UserMore,Prescription,Appointments,CreatePatient
# Create your views here.


def index(request):
    return render(request, 'Hospital_Pages/index.html')

def About(request):
    return render(request,'Hospital_Pages/about.html')


def Register(request):
    form = AddUserForm
    if request.method == 'POST':
        firstname = request.POST['first']
        lastname = request.POST['last']
        userphone = request.POST['user_phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass1']
        conform = request.POST['pass2']
        role = request.POST['category']
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is being used')
            return redirect('register')
        if firstname.isdigit():
            messages.error(request, 'Firstname cannot have numbers')
            return redirect('register')
        if lastname.isdigit():
            messages.error(request, 'Lastname cannot have numbers')
            return redirect('register')
        if regex.search(firstname):
            messages.error(request, 'firstname cannot have special characters')
            return redirect('register')
        if regex.search(lastname):
            messages.error(request, 'lastname cannot have special characters')
            return redirect('register')
        try:
            v = validate_email(email)
            val_email = v["email"]
        except EmailNotValidError as e:
            messages.error(request, 'Invalid Email ID')
            return redirect('register')
        if password != conform:
            messages.error(request, 'Password mismatch')
            return redirect('register')
        # Generating unique id
        num = random.randint(10000000, 99999999)
        str1 = 'VE'
        unique_id = str1 + str(num)
        try:
            user=User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname,
                                     password=password)
            if role == "Doctor":
                user.is_staff = True

                user.save()
                u_id = User.objects.get(username=username)
                addusr = UserDetails(user_id=u_id, user_pass=password, user_phone=userphone, user_role=role)
                addusr.save()
            elif role == 'Patient':
                user.is_staff = False
                user.save()
                u_id = User.objects.get(username=username)
                addusr = UserDetails(user_id=u_id, user_pass=password, user_phone=userphone, user_role=role)
                addusr.save()


        except:
            usr = User.objects.get(username=email)
            usr.delete()
            messages.error(request, 'Some error occured !')
            return redirect('register')
        messages.success(request, 'User Added!')
        return redirect('register')
    context = {
        'form': form
    }
    return render(request, 'Hospital_Pages/register.html', context)

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username=username, password=password)
        # Roles

        if user is not None:
            login(request, user)
            if request.user.is_staff and request.user.is_superuser:
                if user.username == "reception":
                    messages.success(request, "Welcome Receptionalist")
                    return redirect('receptionDash')

            if request.user.is_superuser and not request.user.is_staff:
                messages.success(request,"Welcome HR")
                return redirect('hrDash')
            else:

                if request.user.is_staff and not request.user.is_superuser:
                    messages.success(request, 'Welcome Doctor')
                    return redirect('doctorDash')
                elif request.user.is_active and not request.user.is_superuser:
                    messages.success(request, 'Welcome Patient')
                    return redirect('index')



        messages.error(request, "Login failed")
        return redirect('login')
    return render(request, 'Hospital_Pages/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'Hospital_Pages/logout.html')

def DoctorDashboard(request):

    return render(request,'Doctor_Pages/doctorDashboard.html')

def DoctorProfie(request):
    user = request.user

    details = UserDetails.objects.get(user_id_id=user.pk)

    if request.method == 'POST':
        if 'update' in request.POST:
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            case = request.POST['casePaper']
            blood = request.POST['b-group']
            gender = request.POST['gender']
            age = request.POST['age']
            data = UserMore(user_id_id=details.pk,address1=address1,address2=address2,case=case,blood=blood,gender=gender,age=age)
            data.save()
            messages.success(request,"User Info Updated")
            return redirect('doctorProfile')
        if 'newup' in request.POST:
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            case = request.POST['casePaper']
            age = request.POST['age']
            update = UserMore.objects.get(user_id_id=details.pk)

            update.address1 = address1
            update.address2 =address2
            update.case = case
            update.age = age
            update.save()
            messages.success(request,"Updated Successfully")

    if UserMore.objects.filter(user_id_id=details.pk).exists():
        users = UserMore.objects.get(user_id_id=details.pk)
        context = {
            'details': details,
            'users' :users
        }

        return render(request, 'Doctor_Pages/doctorProfile.html', context)

    context = {
        'details': details,
    }

    return render(request,'Doctor_Pages/doctorProfile.html',context)

def DoctorAppointmnets(request):
    return render(request,'Doctor_Pages/doctorAppointments.html')

def DoctorPrescription(request):
    if request.user.is_active and request.user.is_staff:
        user = request.user
        patients = User.objects.all()
        details = UserDetails.objects.get(user_id_id=user.pk)
        if request.method == "POST":
            if 'addPres' in request.POST:
                prescrip = request.POST['prescrip']
                disease = request.POST['disease']
                patient = request.POST['patient']


                data = Prescription(user_id_id=details.pk,prescrip=prescrip,patient=patient,disease=disease)
                data.save()
                messages.success(request,"Prescription added")



        prescriptions = Prescription.objects.order_by("-create_date")
        context = {
            'press':prescriptions,
            'lists':patients,
        }

        return render(request,'Doctor_Pages/doctorPrescription.html',context)

    else:
        return redirect('login')

# Patient

def PatientMedical(request):
    user = request.user
    p_name = user.first_name+" "+user.last_name
    print(p_name)

    medical = Prescription.objects.filter(patient=p_name)
    context ={
        'medical':medical,
    }
    return render(request,'Patient_Pages/patientMedical.html',context)

def PatientAppoint(request):
    user = request.user

    name = user.first_name+" "+user.last_name
    appoints = Appointments.objects.filter(patient=name)
    context ={
        'appoints':appoints,
    }
    return render(request,"Patient_Pages/appointments.html",context)


def ReceptionDash(request):
    user = request.user

    patients = CreatePatient.objects.filter("create_date")


    appointments = Appointments.objects.order_by("date")

    total = appointments.count()
    done = Appointments.objects.filter(status='Completed')
    t_done = done.count()
    up = Appointments.objects.filter(status='Pending')
    u_done = up.count()


    context ={
        'appoint':appointments,
        'total' : total,
        't_done' :t_done,
        'u_done':u_done,
        'patients':patients,
    }

    return render(request,'Hospital_Pages/receptionDashboard.html',context)

def ReceptionAppointment(request):

    user = request.user
    lists = User.objects.all()

    if request.method == 'POST':
        if 'create' in request.POST:
            date = request.POST['date1']
            time = request.POST['time']
            doctor = request.POST['doctors']
            patient = request.POST['patients']
            status = request.POST['status']

            data = Appointments(date=date,time=time,doctor=doctor,patient=patient,status=status)
            data.save()
            messages.success(request,"Appointement created")
            return redirect('receptionDash')

    context ={
        'lists':lists
    }

    return render(request,'Hospital_Pages/receptionAppointment.html',context)

def ReceptionPatient(request):

    form = AddUserForm

    if request.method == "POST":
        if 'create' in request.POST:
            name = request.POST['name']
            phone = request.POST['user_phone']
            email = request.POST['email']
            gender = request.POST['gender']
            address = request.POST['address']
            outstand = request.POST['outstanding']
            paid = request.POST['paid']
            blood = request.POST['group']
            case = request.POST['case']
            age = request.POST['age']

            data = CreatePatient(name=name,phone=phone,email=email,gender=gender,address=address,out=outstand,
                                 paid=paid,group=blood,case=case,age=age)
            data.save()
            messages.success(request,"Patient Created Successfully")
            return redirect("receptionDash")

    context ={
        'form':form,
    }

    return render(request,"Hospital_Pages/createPatient.html",context)


def hrDash(request):
    user = request.user
    doctors = UserMore.objects.all()
    patients = CreatePatient.objects.order_by('create_date')
    patient = patients.count()
    print(patient)
    context ={
        'patient':patient,
        'more':doctors.count()
    }

    return render(request,"Hospital_Pages/hrDashboard.html",context)