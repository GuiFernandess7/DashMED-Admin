from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Patient, Doctor

class GetPatientsTestCase(APITestCase):

    def setUp(self):
        self.url = reverse("patients") 
        Patient.objects.create(
            name="Maria da Silva",
            sex="F",
            date_of_birth="1985-07-15",
            address="Avenida Principal, 456",
            cep="98765-432",
            rg="98.765.432-1",
            cpf="987.654.321-00",
            phone_number="+55 41 91234-5678"
        ) 

    def test_patient_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

class DoctorTestCase(TestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(
            name="Dr. John Doe",
            specialty="Cardiology",
            rg="123456",
            cpf="123456789",
            crm="CRM/SP 123456",
            contact="1234567890",
            hours_start="09:00:00",
            hours_end="17:00:00"
        )

    def test_doctor_str(self):
        self.assertEqual(str(self.doctor), "Dr. John Doe")

