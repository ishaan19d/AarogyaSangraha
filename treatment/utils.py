from django.shortcuts import resolve_url
def get_login_redirect_url(user):
    if hasattr(user, 'hospital'):
        return resolve_url('treatment:hospital_dashboard', hospitalID=user.hospital.get_hospital_id())
    elif hasattr(user, 'medicalpractitioner'):
        return resolve_url('treatment:practitioner_dashboard',medicalID=user.medicalpractitioner.get_medicalID())
    elif hasattr(user, 'patient'):
        return resolve_url('treatment:patient_dashboard',aadharNo=user.patient.get_aadharNo())
    elif hasattr(user,'admin'):
        return resolve_url('treatment:admin_dashboard',username=user.admin.get_username())
    else:
        return resolve_url('default_redirect_url')