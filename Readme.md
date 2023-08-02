### Doctor-Patient Appointment System

As per the given task, This is a Django and Django REST framework based web application for managing doctor-patient appointments. The system allows users to create and manage doctor and patient records and book appointments between them.

### Setup Instructions

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. Update the project settings:

In `doctor_appointment_system/settings.py`, set the `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to your email credentials for the email notification system.

3. Run database migrations:

```bash
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

## NOTE

#### For all API Endpoints to work we would need Google's credentials, this is just implementation of it.

### API Endpoints

1. **Doctors:**

- `GET /api/doctors/`: Retrieve the list of all doctors.
- `POST /api/doctors/`: Create a new doctor.

Example Doctor payload for POST request:

```json
{
  "name": "Dr. John Doe",
  "phone_number": "1234567890",
  "email": "john.doe@example.com"
}
```

2. **Patients:**

- `GET /api/patients/`: Retrieve the list of all patients.
- `POST /api/patients/`: Create a new patient.

Example Patient payload for POST request:

```json
{
  "name": "Alice Smith",
  "phone_number": "9876543210",
  "email": "alice.smith@example.com"
}
```

3. **Appointments:**

- `GET /api/appointments/`: Retrieve the list of all appointments.
- `POST /api/appointments/`: Create a new appointment.

Example Appointment payload for POST request:

```json
{
  "doctor": 1,
  "patient": 1, 
  "appointment_date": "2023-08-15T10:00:00",
  "description": "Regular check-up"
}