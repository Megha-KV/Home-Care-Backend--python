from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NurseScheduleSerializer, AppointmentSerializer
from .models import NurseSchedule
from doctor_schedule.models import DoctorSchedule
from patientregistration import models as patientModel

class Schedule(APIView):
    model = NurseSchedule
    Model_serializer = NurseScheduleSerializer

    def post(self, request):
        data = request.data
        nurse_id = data.get('nurse_id')
        mr_no = data.get('mr_no')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        existing_doctor_schedules = DoctorSchedule.objects.filter(
            mr_no=mr_no,
            start_date=start_date
        )
        
        if existing_doctor_schedules:
            conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_doctor_schedules]
            # print(f"Conflict dates: {conflict_dates}")  # Debugging: Print conflict dates

            response_data = {
                 'message': f'A doctor is already scheduled for the same patient on the following dates: {", ".join(conflict_dates)}'
}
            # print(f"Response data: {response_data}")  # Debugging: Print response data

            return Response(response_data, status=status.HTTP_409_CONFLICT)


        existing_nurse_schedules = self.model.objects.filter(
            nurse_id=nurse_id,
            mr_no=mr_no,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        )

        if existing_nurse_schedules:
            conflict_dates = [(schedule.start_date.strftime('%Y-%m-%d'), schedule.end_date.strftime('%Y-%m-%d')) for schedule in existing_nurse_schedules]
            message = f'The nurse is already scheduled for the same patient on the same date. Conflicting dates: {", ".join([f"{start} , {end}" for start, end in conflict_dates])}'
            return Response({
                   'message': message
            }, status=status.HTTP_409_CONFLICT)

        other_nurse_schedules = self.model.objects.filter(
            mr_no=mr_no,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        ).exclude(nurse_id=nurse_id)
        
        if other_nurse_schedules:
            conflict_dates = [(schedule.start_date.strftime('%Y-%m-%d'), schedule.end_date.strftime('%Y-%m-%d')) for schedule in other_nurse_schedules]
            message = f'Another nurse is already scheduled for the same patient on the same date. Conflicting dates: {", ".join([f"{start} , {end}" for start, end in conflict_dates])}'
            return Response({
        'message': message
    }, status=status.HTTP_409_CONFLICT)


        other_patient_schedules = self.model.objects.filter(
            nurse_id=nurse_id,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        ).exclude(mr_no=mr_no)

        if other_patient_schedules:
           conflict_dates = [(schedule.start_date.strftime('%Y-%m-%d'), schedule.end_date.strftime('%Y-%m-%d')) for schedule in other_patient_schedules]
           message = f'The nurse is already assigned to another patient on the same date. Conflicting dates: {", ".join([f"{start} , {end}" for start, end in conflict_dates])}'
           return Response({
        'message': message
    }, status=status.HTTP_409_CONFLICT)

        serializer = self.Model_serializer(data=request.data)
        if serializer.is_valid():
            patient = patientModel.Patientregistration.objects.get(mr_no=mr_no)
            serializer.save(
                photo=patient.photo.url,
                patient_name=str(patient.first_name) + ' ' + str(patient.middle_name) + ' ' + str(patient.last_name),
                address=str(patient.address1) + ' ' + str(patient.address2),
                mr_no=patient.mr_no,
                consult_id=patient.consult_id
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        item = self.model.objects.filter(id=request.data.get('id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.Model_serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        item = self.model.objects.filter(id=request.data.get('id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetSchedule(APIView):
    def get(self, request):
        date = request.query_params.get('date')
        nurse_id = request.query_params.get('nurse_id')
        if date:
            items = NurseSchedule.objects.filter(start_date=date, nurse_id=nurse_id)
        else:
            if request.query_params:
                items = NurseSchedule.objects.filter(**request.query_params.dict())
            else:
                items = NurseSchedule.objects.all()

        serializer = AppointmentSerializer(items, many=True)
        return Response(serializer.data)

class CheckScheduleConflict(APIView):
    model = NurseSchedule

    def post(self, request):
        data = request.data
        nurse_id = data.get('nurse_id')
        mr_no = data.get('mr_no')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        
        existing_doctor_schedules = DoctorSchedule.objects.filter(
            mr_no=mr_no,
            start_date=start_date
        )
       
        if existing_doctor_schedules:
            conflict_dates = [schedule.start_date.strftime('%Y-%m-%d') for schedule in existing_doctor_schedules]
            # print(f"Conflict dates: {conflict_dates}")  # Debugging: Print conflict dates

            response_data = {
                 'message': f'A doctor is already scheduled for the same patient on the following dates: {", ".join(conflict_dates)}'
}
            # print(f"Response data: {response_data}")  # Debugging: Print response data

            return Response(response_data, status=status.HTTP_409_CONFLICT)
        
        existing_nurse_schedules = self.model.objects.filter(
            nurse_id=nurse_id,
            mr_no=mr_no,
           start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        )
        
        if existing_nurse_schedules:
            conflict_dates = [(schedule.start_date.strftime('%Y-%m-%d'), schedule.end_date.strftime('%Y-%m-%d')) for schedule in existing_nurse_schedules]
            message = f'The nurse is already scheduled for the same patient on the same date. Conflicting dates: {", ".join([f"{start} , {end}" for start, end in conflict_dates])}'
            return Response({
                   'message': message
            }, status=status.HTTP_409_CONFLICT)
        

        other_nurse_schedules = self.model.objects.filter(
            mr_no=mr_no,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        ).exclude(nurse_id=nurse_id)
        
        if other_nurse_schedules:
            conflict_dates = [(schedule.start_date.strftime('%Y-%m-%d'), schedule.end_date.strftime('%Y-%m-%d')) for schedule in other_nurse_schedules]
            message = f'Another nurse is already scheduled for the same patient on the same date. Conflicting dates: {", ".join([f"{start} , {end}" for start, end in conflict_dates])}'
            return Response({
        'message': message
    }, status=status.HTTP_409_CONFLICT)


        other_patient_schedules = self.model.objects.filter(
            nurse_id=nurse_id,
            start_date__lte=end_date,
            end_date__gte=start_date,
            start_time__lte=end_time,
            end_time__gte=start_time
        ).exclude(mr_no=mr_no)

        if other_patient_schedules:
           conflict_dates = [(schedule.start_date.strftime('%Y-%m-%d'), schedule.end_date.strftime('%Y-%m-%d')) for schedule in other_patient_schedules]
           message = f'The nurse is already assigned to another patient on the same date. Conflicting dates: {", ".join([f"{start} , {end}" for start, end in conflict_dates])}'
           return Response({
        'message': message
    }, status=status.HTTP_409_CONFLICT)

        return Response({'message': 'There is no conflict in schedules'}, status=status.HTTP_200_OK)