from django import forms
from django.contrib.auth.models import User
from . import models
"""
class Hospital(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    hospitalID = models.CharField(max_length=10,primary_key=True)
    address = models.CharField(max_length=250)
    status=models.BooleanField(default=True)"""
class HospitalUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }
class HospitalForm(forms.ModelForm):
    class Meta:
        model=models.Hospital
        fields=['name','hospitalID','address']

class MedicalPractitionerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }
class MedicalPractitionerForm(forms.ModelForm):
    class Meta:
        model=models.MedicalPractitioner
        fields=['medicalID','sex','date_of_birth','department']

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['aadharNo','sex','date_of_birth','bloodGroup','emergencyContact','criticalInfo','bid','did']

class JobApplicationForm(forms.Form):
    hospital = forms.ModelChoiceField(queryset=models.Hospital.objects.all())
    experience = forms.IntegerField(required=True)

#create a form for admin user
class AdminUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }