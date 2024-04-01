from django.contrib import admin
from django.urls import path
from treatment import views
from django.contrib.auth.views import LoginView,LogoutView
app_name='treatment'
urlpatterns = [
    path('hospitalsignup',views.hospital_signup_view,name='hospitalsignup'),
    path('hospitallogin',LoginView.as_view(template_name='treatment/hospitallogin.html'),name='hospitallogin'),
    path('hospitallogout',LogoutView.as_view(next_page='http://127.0.0.1:8000/'),name='hospitallogout'),
    path('hospitaldashboard/<str:hospitalID>',views.hospital_dashboard_view,name='hospital_dashboard'),
    
    path('medpracsignup',views.medical_practitioner_signup_view,name='medpracsignup'),
    path('medpraclogin',LoginView.as_view(template_name='treatment/medpraclogin.html'),name='medpraclogin'),
    path('medpraclogout',LogoutView.as_view(next_page='http://127.0.0.1:8000/'),name='medpraclogout'),
    path('practitionerdashboard/<str:medicalID>',views.medical_practitioner_dashboard_view,name='practitioner_dashboard'),

    path('patientsignup',views.patient_signup_view,name='patientsignup'),
    path('patientlogin',LoginView.as_view(template_name='treatment/patientlogin.html'),name='patientlogin'),
    path('patientlogout',LogoutView.as_view(next_page='http://127.0.0.1:8000/'),name='patientlogout'),
    path('patientdashboard/<str:aadharNo>',views.patient_dashboard_view,name='patient_dashboard'),
    
    path('adminsignup',views.admin_signup_view,name='adminsignup'),
    path('adminlogin',LoginView.as_view(template_name='treatment/adminlogin.html'),name='adminlogin'),
    path('adminlogout',LogoutView.as_view(next_page='http://127.0.0.1:8000/'),name='adminlogout'),
    path('admindashboard/<str:username>',views.admin_dashboard_view,name='admin_dashboard'),

    path('login_redirect/', views.login_redirect_view, name='login_redirect'),

    path('send-job-application/', views.send_job_application, name='send_job_application'),
    path('application-sent/', views.application_sent, name='application_sent'),
    path('process-job-application/<int:application_id>/', views.process_job_application, name='process_job_application'),
    path('job-applications/', views.job_applications, name='job_applications'),

    path('hospital-verification/', views.hospital_verification, name='hospital_verification'),
    path('process-hospital-verification/<str:hospitalID>/', views.process_hospital_verification, name='process_hospital_verification'),

    path('add-treatment',views.add_treatment,name='add_treatment'),
    path('treatment-detail/<str:tid>',views.treatment_detail,name='treatment_detail'),

    path('patient-treatments/',views.patient_treatments,name='patient_treatments'),
    path('raise-query/<str:tid>',views.raise_query,name='raise_query'),
    path('queried-treatments/',views.queried_treatments,name='queried_treatments'),
    path('queried-treatments/<uuid:tid>/terminate/', views.terminate_med_prac, name='terminate_med_prac'),
    path('queried-treatments/<uuid:tid>/reject_query/', views.reject_query, name='reject_query'),

    path('add-medicine',views.add_medicine,name='add_medicine'),
    path('delete-medicine/<str:medName>',views.delete_medicine,name='delete_medicine'),
    path('medicine-list',views.medicine_list,name='medicine_list'),

    path('add-vitals',views.add_vitals,name='add_vitals'),
    path('vitals-list/<str:aadharNo>',views.vitals_list,name='vitals_list'),

    path('requests-suspension-removal/', views.requests_suspension_removal, name='requests_suspension_removal'),
    path('suspension-removal/<str:medicalID>/', views.suspension_removal, name='suspension_removal'),
    path('suspension-permanent/<str:medicalID>',views.suspension_permanent,name='suspension_permanent'),
]