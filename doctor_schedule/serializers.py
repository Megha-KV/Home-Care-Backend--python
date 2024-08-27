from rest_framework import serializers
from .models import DoctorSchedule


class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = ['doctor_id','start_date','end_date','start_time','end_time','photo','address','patient_name','mr_no','consult_id']
        read_only_fields = ['photo', 'address','patient_name','consult_id']

class AppointmentSerializer(serializers.Serializer):
    photo = serializers.CharField()
    start_date = serializers.DateField()
    mr_no  = serializers.CharField()
    consult_id = serializers.CharField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    patient_name = serializers.CharField()
    address = serializers.CharField()
    consult_id = serializers.CharField()