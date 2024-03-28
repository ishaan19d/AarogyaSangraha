from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from .utils import get_login_redirect_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.
def home_view(request):
    patient_count=models.Patient.objects.count()
    medical_count=models.MedicalPractitioner.objects.count()
    hospital_count=models.Hospital.objects.count()
    mydict={'patient_count':patient_count,'medical_count':medical_count,'hospital_count':hospital_count}
    return render(request,'treatment/home.html',context=mydict)

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

def admin_signup_view(request):
    userForm=forms.AdminUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.AdminUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            admin = models.Admin(user=user)
            admin.save()

        return HttpResponseRedirect('adminlogin')
    return render(request,'treatment/adminsignup.html',context=mydict)
    
def hospital_dashboard_view(request,hospitalID):
    hospital=models.Hospital.objects.get(hospitalID=hospitalID)
    return render(request,'treatment/hospital_dashboard.html',{'hospital':hospital})

def patient_dashboard_view(request,aadharNo):
    patient=models.Patient.objects.get(aadharNo=aadharNo)
    return render(request,'treatment/patient_dashboard.html',{'patient':patient})

def medical_practitioner_dashboard_view(request,medicalID):
    medical_practitioner=models.MedicalPractitioner.objects.get(medicalID=medicalID)
    job_application = models.JobApplication.objects.filter(medical_practitioner=medical_practitioner, status='pending')
    return render(request,'treatment/medprac_dashboard.html',{'medicalPractitioner':medical_practitioner, 'job_status': True if job_application else False})

def admin_dashboard_view(request, username):
    user = User.objects.get(username=username)
    admin = user.admin
    return render(request, 'treatment/admin_dashboard.html', {'admin': admin})

def login_redirect_view(request):
    user = request.user
    redirect_url = get_login_redirect_url(user)
    return redirect(redirect_url)

def send_job_application(request):
    if request.method == 'POST':
        form = forms.JobApplicationForm(request.POST)
        if form.is_valid():
            medical_practitioner = request.user.medicalpractitioner
            hospital_id = form.cleaned_data['hospital'].hospitalID
            print(f"Submitted hospital_id: {hospital_id}")
            hospital = get_object_or_404(models.Hospital, hospitalID=hospital_id)
            experience = form.cleaned_data['experience']
            job_application = models.JobApplication.objects.create(
                medical_practitioner=medical_practitioner,
                hospital=hospital,
                experience=experience
            )
            messages.success(request, 'Your job application has been sent successfully.')
            return redirect('treatment:application_sent')
    else:
        form = forms.JobApplicationForm()
    return render(request, 'treatment/send_job_application.html', {'form': form})

def application_sent(request):
    return render(request, 'treatment/application_sent.html')

@login_required
def process_job_application(request, application_id):
    job_application = get_object_or_404(models.JobApplication, id=application_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'accept':
            job_application.status = 'accepted'
            job_application.medical_practitioner.hospitalID = job_application.hospital
            job_application.medical_practitioner.save()
        elif status == 'reject':
            job_application.status = 'rejected'
        job_application.save()
        return redirect('treatment:job_applications')
    return render(request, 'treatment/process_job_application.html', {'job_application': job_application})

@login_required
def job_applications(request):
    hospital = request.user.hospital
    job_applications = models.JobApplication.objects.filter(hospital=hospital)
    return render(request, 'treatment/job_applications.html', {'job_applications': job_applications})

@login_required
def hospital_verification(request):
    hospitals=models.Hospital.objects.filter(status='pending')
    return render(request, 'treatment/hospital_verification.html', {'hospitals': hospitals})

@login_required
def process_hospital_verification(request, hospitalID):
    hospital = get_object_or_404(models.Hospital, hospitalID=hospitalID)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'approve':
            hospital.status = 'approved'
        elif status == 'reject':
            hospital.status = 'rejected'
        hospital.save()
        return redirect('treatment:hospital_verification')
    return render(request, 'treatment/process_hospital_verification.html', {'hospital': hospital})

@login_required
def add_treatment(request):
    if request.method == 'POST':
        form = forms.TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.medicalID = request.user.medicalpractitioner
            treatment.hospitalID = request.user.medicalpractitioner.hospitalID
            treatment.save()
            return redirect('treatment:treatment_detail', tid=treatment.tid)
    else:
        form = forms.TreatmentForm()
    return render(request, 'treatment/add_treatment.html', {'form': form})

def treatment_detail(request, tid):
    treatment = get_object_or_404(models.Treatment, tid=tid)
    return render(request, 'treatment/treatment_detail.html', {'treatment': treatment})

@login_required
def patient_treatments(request):
    treatments = models.Treatment.objects.filter(aadharNo=request.user.patient.get_aadharNo()).order_by('-time')
    return render(request, 'treatment/patient_treatments.html', {'treatments': treatments})

@login_required
def raise_query(request, tid):
    treatment = get_object_or_404(models.Treatment, tid=tid)
    if request.method == 'POST':
        query = request.POST.get('query')
        treatment.query = query
        treatment.save()
        return redirect('treatment:treatment_detail', tid=tid)
    return render(request, 'treatment/raise_query.html', {'treatment': treatment})

@login_required
def queried_treatments(request):
    treatments = models.Treatment.objects.filter(query__in=['Wrong Treatment', 'False Treatment'])
    return render(request, 'treatment/queried_treatments.html', {'treatments': treatments})

@login_required
def terminate_med_prac(request, tid):
    treatment = get_object_or_404(models.Treatment, tid=tid)
    practitioner = get_object_or_404(models.MedicalPractitioner, medicalID=treatment.medicalID.get_medicalID())
    practitioner.hospitalID = None
    treatment.query='Addressed'
    treatment.save()
    practitioner.save()
    return redirect('treatment:queried_treatments')

@login_required
def reject_query(request, tid):
    treatment = get_object_or_404(models.Treatment, tid=tid)
    treatment.query = 'No'
    treatment.save()
    return redirect('treatment:queried_treatments')

@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = forms.MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treatment:add_medicine')
    else:
        form = forms.MedicineForm()
    return render(request, 'treatment/add_medicine.html', {'form': form})

@login_required
def delete_medicine(request, medName):
    medicine = get_object_or_404(models.Medicine, medName=medName)
    medicine.delete()
    return redirect('treatment:medicine_list')

def medicine_list(request):
    medicines = models.Medicine.objects.all()
    return render(request, 'treatment/medicine_list.html', {'medicines': medicines})

@login_required
def add_vitals(request):
    if request.method == 'POST':
        form = forms.VitalsForm(request.POST)
        if form.is_valid():
            vitals = form.save(commit=False)
            vitals.hospitalID = request.user.medicalpractitioner.hospitalID
            vitals.save()
            return redirect('treatment:add_vitals')
    else:
        form = forms.VitalsForm()
    return render(request, 'treatment/add_vitals.html', {'form': form})

def vitals_list(request, aadharNo):
    vitals = models.Vitals.objects.filter(aadharNo=aadharNo).order_by('-time')
    return render(request, 'treatment/vitals_list.html', {'vitals': vitals})