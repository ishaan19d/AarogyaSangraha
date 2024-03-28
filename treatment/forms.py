from django import forms
from django.contrib.auth.models import User
from . import models
from django_select2.forms import ModelSelect2Widget

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

class AdminUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }

class TreatmentForm(forms.ModelForm):
    aadharNo = forms.ModelChoiceField(
        queryset=models.Patient.objects.all(),
        label='Aadhar No',
        to_field_name='aadharNo',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'data-live-search': 'true'
        })
    )
    class Meta:
        model = models.Treatment
        fields = ['disease', 'severity', 'admitted', 'aadharNo', 'treatmentCost','suggestions']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ['medName', 'company', 'type_med', 'regulatoryClass','dosage', 'medCost']