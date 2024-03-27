from django.contrib import admin
from .models import BirthCertificate,DeathCertificate,Hospital,MedicalPractitioner,Patient,Medicine,Treatment,Medicine_Treatment,Vitals,JobApplication,Admin
# Register your models here.
admin.site.register(BirthCertificate)
admin.site.register(DeathCertificate)
admin.site.register(Hospital)
admin.site.register(MedicalPractitioner)
admin.site.register(Patient)
admin.site.register(Medicine)
admin.site.register(Treatment)
admin.site.register(Medicine_Treatment)
admin.site.register(Vitals)
admin.site.register(JobApplication)
admin.site.register(Admin)