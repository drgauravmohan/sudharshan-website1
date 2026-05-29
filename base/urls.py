from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blogdtl, name='blog-detail'),
    path('careers/', views.careers, name='careers'),
    path('contact-us/', views.contact, name='contact-us'),
    path('health-library/', views.health_library, name='health-library'),
    path('home-care/', views.home_care, name='home-care'),
    path('international-patient/', views.international_patient, name='international-patient'),
    path('shc-labs/', views.shc_labs, name='shc-labs'),
    path('our-pharmacy/', views.our_pharmacy, name='our-pharmacy'),
    path('service/<slug:slug>/', views.service_detail, name='service-detail'),
    path('services/', views.services, name='services'),
    path('why-us/', views.why_us, name='why-us'),
    path('second-opinion/', views.contact, name='second-option'),
    path('doctor-listing/', views.contact, name='Find-a-doctor'),
    path('find-a-doctor/', views.contact, name='find-a-doctor'),
    path('patient/terms-conditions/', views.terms_conditions, name='terms-conditions'),
    path('help-desk/', views.help_desk, name='help-desk'),
    path('technology/', views.technology, name='technology'),
    path('ailments/', views.ailments, name='ailments'),
    path('healthcheckup/', views.contact, name='health-checkup'),
    path('healthcheckup/gurugram-hospital/', views.contact, name='health-checkup-old'),

    # Cardiology service pages -> service detail
    path('service/cardiology/', views.cardiology, name='cardiology'),
    path('service/angioplasty/', views.angioplasty, name='angioplasty'),
    path('service/angiography/', views.contact, name='angiography'),
    path('service/echocardiography/', views.contact, name='echocardiography'),
    path('service/ecg/', views.contact, name='ecg'),
    path('service/tmt/', views.contact, name='tmt'),
    path('service/holter/', views.contact, name='holter'),
    path('service/pacemaker/', views.contact, name='pacemaker'),

    # Speciality pages
    path('hospitals-near-me/gurugram-hospital/speciality/cardiology/', views.cardiology, name='cardiology-old'),
    path('hospitals-near-me/gurugram-hospital/speciality/angioplasty/', views.angioplasty, name='angioplasty-old'),
    path('hospitals-near-me/gurugram-hospital/speciality/', views.speciality, name='speciality'),

    # All old hospital pages -> contact
    path('hospitals-near-me/gurugram-hospital/', views.contact, name='hospitals-near-me'),
    path('hospitals-near-me/lucknow-hospital/', views.contact, name='lucknow-hospital'),
    path('hospitals-near-me/patna-hospital/', views.contact, name='patna-hospital'),
    path('hospitals-near-me/indore-hospital/', views.contact, name='indore-hospital'),
    path('hospitals-near-me/noida-hospital/', views.contact, name='noida-hospital'),
    path('hospitals-near-me/ranchi-hospitals/', views.contact, name='ranchi-hospitals'),
    path('mediclinics/', views.contact, name='mediclinics'),

    # International patient broken links -> contact
    path('international-patient/services/request-an-estimate/', views.contact, name='int-estimate'),
    path('plan-your-trip/', views.contact, name='plan-trip'),
    path('international-patient-help-desk/', views.contact, name='int-helpdesk'),
    path('gurugram-360-degree/welcome/', views.contact, name='gurugram-360'),
    path('lucknow-360-degree/welcome/', views.contact, name='lucknow-360'),
    path('patna-360-degree/welcome/', views.contact, name='patna-360'),
    path('treatments/', views.contact, name='treatments'),
    path('contact/', views.contact, name='contact'),

    # Catch-all for any other broken pages
    path('about/', views.about, name='about-2'),
]
