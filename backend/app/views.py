from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, 
                                     ListCreateAPIView,
                                     CreateAPIView)
from rest_framework.views import Response
from rest_framework import status
from .permissions import AdminOrReadOnly, ReadOnly
from .serializers import PatientSerializer, DoctorSerializer
from .models import Patient, Doctor

class BaseDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminOrReadOnly]
    serializer_class = None
    model = None

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BaseListView(ListCreateAPIView):
    permission_classes = [AdminOrReadOnly]
    serializer_class = None
    model = None

    def get(self, request, *args, **kwargs):
        instances = self.model.objects.all()

        if not instances.exists():
            return Response({"detail": f"Nenhum {self.model.__name__.lower()} encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BaseCreateView(CreateAPIView):
    #permission_classes = [AdminOrReadOnly]
    serializer_class = None
    model = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PatientCreateView(BaseCreateView):
    serializer_class = PatientSerializer
    model = Patient

class DoctorCreateView(BaseCreateView):
    serializer_class = DoctorSerializer
    model = Doctor

class PatientDetailView(BaseDetailView):
    serializer_class = PatientSerializer
    model = Patient

class DoctorDetailView(BaseDetailView):
    serializer_class = DoctorSerializer
    model = Doctor

class PatientListView(BaseListView):
    serializer_class = PatientSerializer
    model = Patient

class DoctorListView(BaseListView):
    serializer_class = DoctorSerializer
    model = Doctor
    
""" class PatientCreateView(APIView):

    def post(self, request):
        patient_serializer = PatientSerializer(data=request.data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return Response({"status": "success", "data": patient_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": patient_serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        
class DoctorCreateView(APIView):

    def post(self, request):
        doctor_serializer = DoctorSerializer(data=request.data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return Response({"status": "success", "data": doctor_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": doctor_serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST) """
        

""" class PatientDetailView(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        selected_patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(selected_patient, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        selected_patient = get_object_or_404(Patient, pk=pk)
        selected_patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """

""" class DoctorDetailView(APIView):
    permission_classes = [AdminOrReadOnly] 

    def get(self, request, pk):
        doctor_selected = Doctor.objects.get(pk=pk)
        doctor_serializer = DoctorSerializer(doctor_selected)
        return Response(doctor_serializer.data)

    def put(self, request, pk):
        doctor_selected = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor_selected, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        selected_doctor = get_object_or_404(Doctor, pk=pk)
        selected_doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
    
""" class PatientListView(APIView):
    permission_classes = [AdminOrReadOnly] 

    def get(self, request):
        patients = Patient.objects.all()

        if not patients.exists():
            return Response({"detail": "Nenhum paciente encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        patient_serializer = PatientSerializer(patients, many=True)
        return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
    
class DoctorListView(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        doctors = Doctor.objects.all()

        if not doctors.exists():
            return Response({"detail": "Nenhum médico encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        doctors_serializer = DoctorSerializer(doctors, many=True)
        return Response(doctors_serializer.data, status=status.HTTP_201_CREATED) """
