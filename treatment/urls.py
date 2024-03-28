from django.contrib import admin
from django.urls import path
from treatment import views
from django.contrib.auth.views import LoginView,LogoutView
app_name='treatment'
urlpatterns = [
    path('hospitalsignup',views.hospital_signup_view,name='hospitalsignup'),
    path('hospitallogin',LoginView.as_view(template_name='treatment/hospitallogin.html'),name='hospitallogin'),
    path('hospitallogout',LogoutView.as_view(template_name='treatment/home.html'),name='hospitallogout'),
    path('hospitaldashboard/<str:hospitalID>',views.hospital_dashboard_view,name='hospital_dashboard'),
    
    path('medpracsignup',views.medical_practitioner_signup_view,name='medpracsignup'),
    path('medpraclogin',LoginView.as_view(template_name='treatment/medpraclogin.html'),name='medpraclogin'),
    path('medpraclogout',LogoutView.as_view(template_name='treatment/home.html'),name='medpraclogout'),
    path('practitionerdashboard/<str:medicalID>',views.medical_practitioner_dashboard_view,name='practitioner_dashboard'),

    path('patientsignup',views.patient_signup_view,name='patientsignup'),
    path('patientlogin',LoginView.as_view(template_name='treatment/patientlogin.html'),name='patientlogin'),
    path('patientlogout',LogoutView.as_view(template_name='treatment/home.html'),name='patientlogout'),
    path('patientdashboard/<str:aadharNo>',views.patient_dashboard_view,name='patient_dashboard'),
    
    path('adminsignup',views.admin_signup_view,name='adminsignup'),
    path('adminlogin',LoginView.as_view(template_name='treatment/adminlogin.html'),name='adminlogin'),
    path('adminlogout',LogoutView.as_view(template_name='treatment/home.html'),name='adminlogout'),
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
]