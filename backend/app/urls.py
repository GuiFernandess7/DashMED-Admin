from django.contrib import admin
from django.urls import path, include
from .views import (PatientListView, 
                    PatientDetailView, 
                    PatientCreateView,
                    DoctorListView,
                    DoctorDetailView
                )

urlpatterns = [
    path("patients/", PatientListView.as_view(), name="patients"),
    path("patient/<int:pk>", PatientDetailView.as_view(), name="patient_detail"),
    path("patient/add", PatientCreateView.as_view(), name="patient_add"),
    path("doctors/", DoctorListView.as_view(), name="doctors")
]