# appointments/urls.py

from django.urls import path
from .views import DoctorListCreateView, PatientListCreateView, AppointmentListCreateView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
]
