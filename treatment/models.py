from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Hospital(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    hospitalID = models.CharField(max_length=10,primary_key=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending Verification'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ), default='pending')

    def get_hospital_id(self):
        return self.hospitalID
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.hospitalID})"

    
departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('General Physician','General Physician'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
('Gynecologist','Gynecologist'),
('Pediatrician','Pediatrician'),
('Dermatologist','Dermatologist'),
('Neurologist','Neurologist'),
('Psychiatrist','Psychiatrist'),
('Nephrologist','Nephrologist'),
('Dentist','Dentist'),
('Nurse','Nurse'),
]
sex_c=[('M','M'),('F','F'),('O','O')]
class MedicalPractitioner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    medicalID = models.CharField(max_length=10,primary_key=True)
    sex = models.CharField(max_length=1,choices=sex_c,default=None)
    date_of_birth = models.DateField()
    hospitalID = models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True,blank=True,to_field='hospitalID')
    department = models.CharField(max_length=50,choices=departments,default=None)
    status = models.CharField(max_length=21, choices=(
        ('Authorized','Authorized'),
        ('Suspended','Suspended'),
        ('Permanently Suspended','Permanently Suspended')
    ), default='Authorized')

    def get_medicalID(self):
        return self.medicalID
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.medicalID})"

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def get_username(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username

bg=[('A+','A+'),('B+','B+'),('AB+','AB+'),('O+','O+'),('A-','A-'),('B-','B-'),('AB-','AB-'),('O-','O-')]
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aadharNo = models.CharField(max_length=12,primary_key=True)
    sex = models.CharField(max_length=1,choices=sex_c,default=None)
    date_of_birth = models.DateField()
    bloodGroup = models.CharField(max_length=3,choices=bg,default=None)
    emergencyContact = models.CharField(max_length=11)
    criticalInfo = models.CharField(max_length=150,null=True,blank=True,default=None)

    def get_aadharNo(self):
        return self.aadharNo
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.aadharNo})"

rclass=[('General','General'),('Restricted','Restricted')]
mtype = [('Antipyretic', 'Antipyretic'),
        ('Analgesic', 'Analgesic'),
        ('Antihistamine', 'Antihistamine'),
        ('Antibiotic', 'Antibiotic'),
        ('Antidepressant', 'Antidepressant'),
        ('Anticoagulant', 'Anticoagulant'),
        ('Antihypertensive', 'Antihypertensive'),
        ('Anti-inflammatory', 'Anti-inflammatory'),
        ('Antiviral', 'Antiviral'),
        ('Diuretic', 'Diuretic'),
        ('Antifungal','Antifungal'),
        ('Antiemetic','Antiemetic'),
        ('Anticonvulsant','Anticonvulsant'),
        ('Bronchodilator','Bronchodilator'),
        ('Muscle Relaxant','Muscle Relaxant'),
        ('Laxative','Laxative'),
        ('Antacid','Antacid'),
        ('Hormone Replacement Therapy (HRT)','Hormone Replacement Therapy (HRT)'),
        ('Immunosuppressant','Immunosuppressant'),
        ('Antimigraine','Antimigraine'),
        ('Antidiabetic','Antidiabetic'),
]
class Medicine(models.Model):
    medName = models.CharField(max_length=100,primary_key=True)
    company = models.CharField(max_length=50)
    type_med = models.CharField(max_length=50,choices=mtype,default=None)
    regulatoryClass = models.CharField(max_length=50,choices=rclass,default=None)
    dosage = models.IntegerField()
    medCost = models.IntegerField()

    def __str__(self):
        return f"{self.medName} ({self.dosage}mg)"

aList = [('Yes', 'Yes'), ('No', 'No'), ('Not Required', 'Not Required')]
q=[('Wrong Treatment','Wrong Treatment'),('False Treatment','False Treatment'),('No','No'),('Addressed','Addressed')]
class Treatment(models.Model):
    tid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=500)
    advisedTest = models.CharField(max_length=250,default=None,null=True,blank=True)
    disease = models.CharField(max_length=75)
    admitted = models.CharField(max_length=20, choices=aList, default='Not Required')
    aadharNo = models.ForeignKey(Patient,on_delete=models.CASCADE,to_field='aadharNo')
    treatmentCost = models.IntegerField()
    medicalID = models.ForeignKey(MedicalPractitioner,on_delete=models.SET_NULL,null=True,blank=True,to_field='medicalID')
    hospitalID = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, to_field='hospitalID')
    suggestions = models.CharField(max_length=500,null=True,blank=True,default=None)
    query = models.CharField(max_length=20,choices=q,default='No')
    medicines = models.ManyToManyField(Medicine, through='Medicine_Treatment')

class Medicine_Treatment(models.Model):
    medName = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True, blank=True, to_field='medName', related_name='treatment_medicines')
    tid = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True, blank=True, to_field='tid', related_name='treatment_medicines')

class Vitals(models.Model):
    hospitalID = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, to_field='hospitalID')
    aadharNo = models.ForeignKey(Patient,on_delete=models.CASCADE,to_field='aadharNo')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    pulse = models.IntegerField()
    bp_High = models.IntegerField()
    bp_low = models.IntegerField()
    spO2 = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    bsa = models.DecimalField(max_digits=5, decimal_places=2)
    glucose = models.IntegerField()
    abnormalities = models.CharField(max_length=100,default=None,null=True,blank=True)

class JobApplication(models.Model):
    medical_practitioner = models.ForeignKey(MedicalPractitioner, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    experience = models.IntegerField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ), default='pending')