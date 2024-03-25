from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hospital(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    hospitalID = models.CharField(max_length=10,primary_key=True)
    address = models.CharField(max_length=250)
    status=models.BooleanField(default=True)

    def get_hospital_id(self):
        return self.hospitalID
    # @property
    # def get_name(self):
    #     return self.user.name
    # @property
    # def get_id(self):
    #     return self.user.id
    # def __str__(self):
    #     return "{} ({})".format(self.user.name,self.hospitalID)
    
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

    def get_medicalID(self):
        return self.medicalID
    # @property
    # def get_name(self):
    #     return self.user.first_name+" "+self.user.last_name
    # @property
    # def get_id(self):
    #     return self.user.id
    # def __str__(self):
    #     return "{} ({})".format(self.user.first_name+" "+self.user.last_name,self.department)

class BirthCertificate(models.Model):
    bid = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=100)
    date_time_birth = models.DateTimeField()
    sex = models.CharField(max_length=1,choices=sex_c,default=None)
    place_birth = models.CharField(max_length=50)
    mothersName = models.CharField(max_length=50)
    fathersName = models.CharField(max_length=50,null=True,blank=True)
    religion = models.CharField(max_length=15,null=True,blank=True)
    hospitalID = models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True,blank=True,to_field='hospitalID',default=None)

class DeathCertificate(models.Model):
    did = models.CharField(max_length=15,primary_key=True)
    bid = models.ForeignKey(BirthCertificate,on_delete=models.CASCADE,to_field='bid')
    date_time_death = models.DateTimeField()
    place_death = models.CharField(max_length=50)
    cause = models.CharField(max_length=150)
    hospitalID = models.ForeignKey(Hospital,on_delete=models.SET_NULL,null=True,blank=True,to_field='hospitalID',default=None)

bg=[('A+','A+'),('B+','B+'),('AB+','AB+'),('O+','O+'),('A-','A-'),('B-','B-'),('AB-','AB-'),('O-','O-'),]
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aadharNo = models.CharField(max_length=12,primary_key=True)
    sex = models.CharField(max_length=1,choices=sex_c,default=None)
    date_of_birth = models.DateField()
    bloodGroup = models.CharField(max_length=3,choices=bg,default=None)
    emergencyContact = models.CharField(max_length=10)
    criticalInfo = models.CharField(max_length=150)
    bid = models.ForeignKey(BirthCertificate,on_delete=models.SET_NULL,null=True,blank=True,to_field='bid',default=None)
    did = models.ForeignKey(DeathCertificate,on_delete=models.SET_NULL,null=True,blank=True,to_field='did',default=None)

    def get_aadharNo(self):
        return self.aadharNo
    # @property
    # def get_name(self):
    #     return self.user.first_name+" "+self.user.last_name
    # @property
    # def get_id(self):
    #     return self.user.id
    # def __str__(self):
    #     return self.user.first_name+" ("+self.aadharNo+")"

rclass=[('general','general'),('restricted','restricted')]
mtype=[('antipyretic','antipyretic'),
       ('analgesic','aanalgesic'),
       ('antihistamine','antihistamine'),
       ('antibiotic','antibiotic'),
       ('antidepressant','antidepressant'),
       ('anticoagulant','anticoagulant'),
       ('antihypertensive','antihypertensive'),
       ('anti-inflammatory','anti-inflammatory'),
       ('antiviral','antiviral'),
       ('diuretic','diuretic')]
class Medicine(models.Model):
    medName = models.CharField(max_length=100,primary_key=True)
    company = models.CharField(max_length=50)
    type_med = models.CharField(max_length=50,choices=mtype,default=None)
    regulatoryClass = models.CharField(max_length=50,choices=rclass,default=None)
    medCost = models.IntegerField()
    # @property
    # def get_it(self):
    #     return self.medName
    # def __str__(self):
    #     return self.medName+" ("+self.type_med+")"

sList=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
aList = [('Yes', 'Yes'), ('No', 'No'), ('Not Required', 'Not Required')]
class Treatment(models.Model):
    tid = models.CharField(max_length=15,primary_key=True)
    date = models.DateField()
    disease = models.CharField(max_length=75)
    severity = models.IntegerField(choices=sList,default=0)
    admitted = models.CharField(max_length=20, choices=aList, default='Not Required')
    aadharNo = models.ForeignKey(Patient,on_delete=models.CASCADE,to_field='aadharNo')
    treatmentCost = models.IntegerField()
    medicalID = models.ForeignKey(MedicalPractitioner,on_delete=models.SET_NULL,null=True,blank=True,to_field='medicalID')
    hospitalID = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, to_field='hospitalID')

class Medicine_Treatment(models.Model):
    medName = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True, blank=True, to_field='medName', related_name='treatment_medicines')
    tid = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True, blank=True, to_field='tid', related_name='treatment_medicines')

class Vitals(models.Model):
    hospitalID = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, to_field='hospitalID')
    aadharNo = models.ForeignKey(Patient,on_delete=models.CASCADE,to_field='aadharNo')
    date = models.DateField()
    time = models.TimeField()
    pulse = models.IntegerField()
    bp_High = models.IntegerField()
    bp_low = models.IntegerField()
    spO2 = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    bsa = models.DecimalField(max_digits=5, decimal_places=2)
    glucose = models.IntegerField()
    abnormalities = models.CharField(max_length=100,default=None,null=True,blank=True)
