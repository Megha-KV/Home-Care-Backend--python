from rest_framework import serializers
from .models import Patientregistration
from drf_extra_fields.fields import Base64ImageField

class PatientregistrationSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Patientregistration
        fields = '__all__'
