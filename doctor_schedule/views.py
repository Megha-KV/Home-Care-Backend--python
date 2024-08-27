from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorScheduleSerializer,AppointmentSerializer
from .models import DoctorSchedule
from django.db import DatabaseError
from patientregistration import models as patientModel
from rest_framework.decorators import api_view
from django.db.models import F




class DoctorScheduleView(APIView):
    model = DoctorSchedule
    Model_serializer =DoctorScheduleSerializer
    
    def post(self, request):
        data = request.data
        doctor_id = data.get('doctor_id')
        mr_no = data.get('mr_no')  # Assuming mr_no is the patient's unique identifier
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        # Check if the current doctor is scheduled for the same patient on the same date
        existing_schedules_current_doctor = self.model.objects.filter(
            doctor_id=doctor_id,
            mr_no=mr_no,
            start_date=start_date
        )

        if existing_schedules_current_doctor:
            conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_schedules_current_doctor]
            return Response({
        'message': f'The current doctor is already scheduled for the patient on the following date: {", ".join(conflict_dates)}'
    }, status=status.HTTP_409_CONFLICT)

        # Check if any other doctor is scheduled for the same patient on the same date
        existing_schedules_other_doctor = self.model.objects.filter(
            mr_no=mr_no,
            start_date=start_date
        ).exclude(doctor_id=doctor_id)

        if existing_schedules_other_doctor:
           conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_schedules_other_doctor]
           return Response({
        'message': f'Another doctor is already scheduled for the patient on the following date: {", ".join(conflict_dates)}'
    }, status=status.HTTP_409_CONFLICT)
        

        existing_schedules = self.model.objects.filter(
            doctor_id=doctor_id,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        )

        if existing_schedules:
           conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_schedules]
           return Response({
        'message': f'The  doctor is already scheduled for a patient on the following date: {", ".join(conflict_dates)}'
    }, status=status.HTTP_409_CONFLICT)
        

        serializer = self.Model_serializer(data=request.data)
        if serializer.is_valid():
            patient = patientModel.Patientregistration.objects.get( mr_no=  mr_no)
            serializer.save(photo = patient.photo.url,patient_name = str(patient.first_name)+' '+str(patient.middle_name)+' '+str(patient.last_name),address = str(patient.address1 )+ ' ' + str(patient.address2),mr_no = patient.mr_no,consult_id = patient.consult_id )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                

    def put(self, request):
            item =self.model.objects.filter(id=request.data.get('id')).first()
            if not item:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer =  self.Model_serializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
            item =self.model.objects.filter(id=request.data.get('id')).first()
            if not item:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetScheduleDoctor(APIView):
    def get(self, request):
        date = request.query_params.get('date')
        doctor_id = request.query_params.get('doctor_id')
        if date:
            # Filter DoctorSchedule instances where date and start_date are the same
            items = DoctorSchedule.objects.filter(start_date=date, doctor_id = doctor_id)
        else:
            if request.query_params:
                items = DoctorSchedule.objects.filter(**request.query_params.dict())
            else:
                items = DoctorSchedule.objects.all()

        serializer = AppointmentSerializer(items, many=True)
        return Response(serializer.data)

class CheckScheduleConflict(APIView):
    model = DoctorSchedule
    
    def post(self, request):
        data = request.data
        doctor_id = data.get('doctor_id')
        mr_no = data.get('mr_no')  # Assuming mr_no is the patient's unique identifier
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        # Check if the current doctor is scheduled for the same patient on the same date
        existing_schedules_current_doctor = self.model.objects.filter(
            doctor_id=doctor_id,
            mr_no=mr_no,
            start_date=start_date
        )

        if existing_schedules_current_doctor:
           conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_schedules_current_doctor]
           return Response({
        'message': f'The current doctor is already scheduled for the patient on the following date: {", ".join(conflict_dates)}'
    }, status=status.HTTP_409_CONFLICT)     
        # Check if any other doctor is scheduled for the same patient on the same date
        existing_schedules_other_doctor = self.model.objects.filter(
            mr_no=mr_no,
            start_date=start_date
        ).exclude(doctor_id=doctor_id)

        if existing_schedules_other_doctor:
          conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_schedules_other_doctor]
          return Response({
        'message': f'Another doctor is already scheduled for the patient on the following date: {", ".join(conflict_dates)}'
    }, status=status.HTTP_409_CONFLICT)
        

        existing_schedules = self.model.objects.filter(
            doctor_id=doctor_id,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        )

        if existing_schedules:
           conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_schedules]
           return Response({
        'message': f'The  doctor is already scheduled for a patient on the following date: {", ".join(conflict_dates)}'
    }, status=status.HTTP_409_CONFLICT)
        return Response({'message': 'There is no conflict in schedules'}, status=status.HTTP_200_OK)