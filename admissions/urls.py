from django.urls import path
from . import views

app_name = 'admissions'
urlpatterns = [
    path('', views.admission_info, name='info'),
    path('inquiry/', views.application_inquiry, name='inquiry'),
]