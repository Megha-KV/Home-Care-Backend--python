from rest_framework import serializers
from .models import NurseSchedule


class NurseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseSchedule
        fields = ['nurse_id','start_date','end_date','start_time','end_time','photo','address','patient_name','mr_no','consult_id']
        read_only_fields = ['photo', 'address','patient_name','consult_id']

class AppointmentSerializer(serializers.Serializer):
    photo = serializers.CharField()
    start_date = serializers.DateField()
    mr_no  = serializers.CharField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    patient_name = serializers.CharField()
    address = serializers.CharField()
    consult_id = serializers.CharField()