from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from .utils import get_login_redirect_url
# Create your views here.
def home_view(request):
    return render(request,'treatment/home.html')

def hospital_signup_view(request):
    userForm=forms.HospitalUserForm()
    hospitalForm=forms.HospitalForm()
    mydict={'userForm':userForm,'hospitalForm':hospitalForm}
    if request.method=='POST':
        userForm=forms.HospitalUserForm(request.POST)
        hospitalForm=forms.HospitalForm(request.POST,request.FILES)
        if userForm.is_valid() and hospitalForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            hospital=hospitalForm.save(commit=False)
            hospital.user=user
            hospital=hospital.save()
            my_hospital_group = Group.objects.get_or_create(name='HOSPITAL')
            my_hospital_group[0].user_set.add(user)
        return HttpResponseRedirect('hospitallogin')
    return render(request,'treatment/hospitalsignup.html',context=mydict)

def medical_practitioner_signup_view(request):
    userForm=forms.MedicalPractitionerUserForm()
    medicalPractitionerForm=forms.MedicalPractitionerForm()
    mydict={'userForm':userForm,'medicalPractitionerForm':medicalPractitionerForm}
    if request.method=='POST':
        userForm=forms.MedicalPractitionerUserForm(request.POST)
        medicalPractitionerForm=forms.MedicalPractitionerForm(request.POST,request.FILES)
        if userForm.is_valid() and medicalPractitionerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            medicalPractitioner=medicalPractitionerForm.save(commit=False)
            medicalPractitioner.user=user
            medicalPractitioner=medicalPractitioner.save()
            my_medical_practitioner_group = Group.objects.get_or_create(name='MEDICAL_PRACTITIONER')
            my_medical_practitioner_group[0].user_set.add(user)
        return HttpResponseRedirect('medpraclogin')
    return render(request,'treatment/medpracsignup.html',context=mydict)

def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'treatment/patientsignup.html',context=mydict)

def hospital_dashboard_view(request,hospitalID):
    hospital=models.Hospital.objects.get(hospitalID=hospitalID)
    return render(request,'treatment/hospital_dashboard.html',{'hospital':hospital})

def patient_dashboard_view(request,aadharNo):
    patient=models.Patient.objects.get(aadharNo=aadharNo)
    return render(request,'treatment/patient_dashboard.html',{'patient':patient})

def medical_practitioner_dashboard_view(request,medicalID):
    medicalPractitioner=models.MedicalPractitioner.objects.get(medicalID=medicalID)
    return render(request,'treatment/medical_practitioner_dashboard.html',{'medicalPractitioner':medicalPractitioner})
def login_redirect_view(request):
    user = request.user
    redirect_url = get_login_redirect_url(user)
    return redirect(redirect_url)