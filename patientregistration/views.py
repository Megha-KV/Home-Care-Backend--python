from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientregistrationSerializer 
from .models import Patientregistration
from nurse_schedule import models as nurseModels
from doctor_schedule import models as doctorModels
from django.db import DatabaseError
from rest_framework.decorators import api_view

class Patient(APIView):
    model = Patientregistration
    serializer_class = PatientregistrationSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
    
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    def get(self, request):
        mr_no= request.query_params.get('mr_no')
        if mr_no:
            try:
                item = Patientregistration.objects.get(mr_no=mr_no)
                serializer = PatientregistrationSerializer(item)
                return Response(serializer.data)
            except Patientregistration.DoesNotExist:
                return Response({'error': 'Patient with provided MRN not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'MRN parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            mr_no = request.data.get('mr_no')  
            item = self.model.objects.filter(mr_no=mr_no).first()  
            if not item:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(item, data=request.data,partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            mr_no = request.data.get('mr_no')
            item = self.model.objects.filter(mr_no=mr_no).first()
            if not item:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetDataAPIView(APIView):
    model = Patientregistration
    Model_serializer = PatientregistrationSerializer

    def get(self, request):
        if request.query_params:
            items = self.model.objects.filter(**request.query_params.dict())
        else:
            items = self.model.objects.all()
            
        serializer =  self.Model_serializer(items, many=True)
        return Response(serializer.data)
