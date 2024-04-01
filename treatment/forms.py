from django import forms
from django.contrib.auth.models import User
from . import models

class HospitalUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,label='Name')
    last_name = forms.ChoiceField(choices=[('Govt. Hospital', 'Govt. Hospital'), ('Pvt. Hospital', 'Pvt. Hospital'),('NGO Hospital','NGO Hospital'),('Pvt. Clinic','Pvt. Clinic')], label='Type')
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }
class HospitalForm(forms.ModelForm):
    class Meta:
        model=models.Hospital
        fields=['hospitalID','address','city','state','pincode']

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
        fields=['aadharNo','sex','date_of_birth','bloodGroup','emergencyContact','criticalInfo']

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
    medicines = forms.ModelMultipleChoiceField(
        queryset=models.Medicine.objects.all(),
        label='Medicines',
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = models.Treatment
        fields = ['symptoms', 'disease','advisedTest', 'admitted', 'aadharNo', 'treatmentCost', 'suggestions', 'medicines']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = ['medName', 'company', 'type_med', 'regulatoryClass','dosage', 'medCost']

class VitalsForm(forms.ModelForm):
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
        model = models.Vitals
        fields = ['aadharNo','pulse', 'bp_High', 'bp_low', 'spO2', 'weight', 'bmi', 'bsa', 'glucose', 'abnormalities']