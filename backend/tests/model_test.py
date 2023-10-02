from django.test import TestCase
from app.models import Patient, Doctor

class PatientModelTest(TestCase):
    def test_patient_str_representation(self):
        patient = Patient(name="John Doe", sex="M", date_of_birth="1990-01-01", address="123 Street",
                          cep="12345-678", rg="1234567", cpf="12345678910", phone_number="1234567890")
        self.assertEqual(str(patient), "John Doe")

    # Adicione mais testes para o modelo Patient conforme necessário

class DoctorModelTest(TestCase):
    def test_doctor_str_representation(self):
        doctor = Doctor(name="Dr. Smith", specialty="Cardiology", rg="1234567", cpf="12345678910",
                        crm="CRM/SP 123456", contact="1234567890", hours_start="09:00:00", hours_end="17:00:00")
        self.assertEqual(str(doctor), "Dr. Smith")

    # Adicione mais testes para o modelo Doctor conforme necessário

