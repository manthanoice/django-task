from django.core.mail import send_mail
from rest_framework import generics
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import timedelta
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        doctor = Doctor.objects.get(pk=instance.doctor.id)
        patient = Patient.objects.get(pk=instance.patient.id)

        # Send email notification to doctor
        send_mail(
            'New Appointment',
            f'Hi {doctor.name}, you have a new appointment with {patient.name} on {instance.appointment_date}.',
            'default_email@gmail.com',
            [doctor.email],  
            fail_silently=False,
        )

        # Send email notification to patient
        send_mail(
            'Appointment Confirmation',
            f'Hi {patient.name}, your appointment with {doctor.name} is confirmed on {instance.appointment_date}.',
            'default_email@gmail.com',
            [patient.email], 
            fail_silently=False,
        )
        credentials = Credentials.from_authorized_user_file('your_google_calendar_credentials.json')  
        service = build('calendar', 'v3', credentials=credentials)

        event = {
            'summary': f'Appointment with {instance.patient_name}',
            'description': instance.description,
            'start': {
                'dateTime': instance.appointment_date.isoformat(),
                'timeZone': 'your_timezone',
            },
            'end': {
                'dateTime': (instance.appointment_date + timedelta(hours=1)).isoformat(),
                'timeZone': 'your_timezone',
            },
        }
        service.events().insert(calendarId='primary', body=event).execute()

        event['summary'] = f'Appointment with {instance.doctor_name}'
