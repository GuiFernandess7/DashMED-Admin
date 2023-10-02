from django.db import models
from django.utils.translation import gettext_lazy as regex
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
import re

PHONE_REGEX = r'^(?:(?:\+|00)?(55)\s?)?(?:\(?([1-9][0-9])\)?\s?)?(?:((?:9\d|[2-9])\d{3})\-?(\d{4}))$'
CEP_REGEX = r'^\d{5}[-.\s]?\d{3}$'
RG_REGEX = r'(^\d{1,2}).?(\d{3}).?(\d{3})-?(\d{1}|X|x$)'
CPF_REGEX = r'^(\d{3}\.\d{3}\.\d{3}-\d{2})$'

class Patient(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    image = models.ImageField(name="photo", upload_to="./assets/", 
                              help_text="Upload a profile image",
                              height_field=None, width_field=None, max_length=100,
                              blank=True, null=True) # Atualizar
    name = models.CharField(max_length=40, null=False, blank=False)
    sex = models.CharField(choices=SEX_CHOICES, null=False, blank=False, max_length=1)
    date_of_birth = models.DateField(blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)
    cep = models.CharField(max_length=15, blank=False, null=True,
                           validators=[RegexValidator(CEP_REGEX)])
    rg = models.CharField(max_length=25, blank=False, null=True,
                           validators=[RegexValidator(RG_REGEX)])
    cpf = models.CharField(max_length=25, blank=False, null=True,
                           validators=[RegexValidator(CPF_REGEX)])
    phone_number = models.CharField(max_length=20, blank=False, null=False,
                                    validators=[RegexValidator(PHONE_REGEX)],
                                    help_text=("Formato: xx xxxxx-xxxx"))
    emergency_contact = models.CharField(max_length=15, blank=True, null=True,
                                    validators=[RegexValidator(PHONE_REGEX)],
                                    help_text=("Formato: xx xxxxx-xxxx"))
    
    def __str__(self):
        return f'{self.name}'

class Doctor(models.Model):
    image = models.ImageField(name="photo", upload_to="./assets/", 
                              help_text="Upload a profile image",
                              height_field=None, width_field=None, max_length=100,
                              blank=True, null=True) # Atualizar
    name = models.CharField(max_length=40, null=False, blank=False)
    specialty = models.CharField(max_length=150)
    rg = models.CharField(max_length=25, blank=False, null=True,
                           validators=[RegexValidator(RG_REGEX)])
    cpf = models.CharField(max_length=25, blank=False, null=True,
                           validators=[RegexValidator(CEP_REGEX)])
    crm = models.CharField(max_length=15, null=False, blank=False, 
                           validators=[RegexValidator(r'^CRM/[A-Z]{2}\s\d{6}$')])
    contact = models.CharField(max_length=30, blank=False, null=False,
        validators=[RegexValidator(PHONE_REGEX)])
    hours_start = models.TimeField(null=False, blank=False)
    hours_end = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

""" class Appointment(models.Model):
    pacient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=False, blank=False)
    doctor = models.ForeignKey(Doctor, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    prescription = models.TextField(blank=False, null=False)
    medications = models.ManyToManyField('Medication', blank=True)

    def __str__(self):
        return f"Consulta - {self.doctor}"

class Medication(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    dosage = models.CharField(max_length=200, null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class MedicalSchedule(models.Model):
    APPOINTMENT_CHOICES = [
        ('consulta', 'Consulta'),
        ('exame', 'Exame'),
        ('cirurgia', 'Cirurgia'),
    ]
    APPOINTMENT_STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    appointment_type = models.CharField(max_length=100, choices=APPOINTMENT_CHOICES, default='consulta')
    appointment_status = models.CharField(max_length=50, choices=APPOINTMENT_STATUS_CHOICES, default='agendado')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'Medical Schedule for {self.patient.name}'

class MedicalExam(models.Model):
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    exam_date_and_time = models.DateTimeField()
    exam_type = models.CharField(max_length=100)  # Tipo de exame (raio-x, ressonância magnética, análise de sangue, etc.)
    exam_results = models.TextField() 
    medical_notes = models.TextField()  

class MedicalHistory(models.Model):
    event_date = models.DateField()  
    event_description = models.TextField()  # Descrição do evento (cirurgias, hospitalizações, alergias, etc.)
    responsible_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  

class InvoiceAndPayments(models.Model):
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)  
    invoice_date = models.DateField()  
    payment_status = models.CharField(max_length=50)  
    payment_methods = models.CharField(max_length=100)  

class StatisticalData(models.Model):
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_collection_date_and_time = models.DateTimeField()  
    data_type = models.CharField(max_length=100)  # Tipo de dado (por exemplo, pressão arterial, nível de glicose, frequência cardíaca)
    numeric_value = models.FloatField()  # Valor numérico do dado
    unit_of_measure = models.CharField(max_length=20, 
                                    validators=[RegexValidator(r'^\d+(\.\d+)?\s*(mmHg|mg/dL|bpm|°C|L/min|kg|mm|cm|s)$')])  # Unidade de medida (mmHg, mg/dL, batimentos por minuto, etc.)
 """