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
#will write index and int and then display one detail of hospital to check
    path('medpracsignup',views.medical_practitioner_signup_view,name='medpracsignup'),
    path('medpraclogin',LoginView.as_view(template_name='treatment/medpraclogin.html'),name='medpraclogin'),
    path('medpraclogout',LogoutView.as_view(template_name='treatment/home.html'),name='medpraclogout'),
    path('practitionerdashboard',views.medical_practitioner_dashboard_view,name='practitioner_dashboard'),

    path('patientsignup',views.patient_signup_view,name='patientsignup'),
    path('patientlogin',LoginView.as_view(template_name='treatment/patientlogin.html'),name='patientlogin'),
    path('patientlogout',LogoutView.as_view(template_name='treatment/home.html'),name='patientlogout'),
    path('patientdashboard',views.patient_dashboard_view,name='patient_dashboard'),
    
    path('login_redirect/', views.login_redirect_view, name='login_redirect'),
]