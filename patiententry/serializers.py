from rest_framework import serializers
from .models import Entry

class PatientEntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    nurse_name = serializers.CharField(read_only = True)
    date = serializers.DateTimeField(read_only = True) 

    class Meta:
        model = Entry
        fields = ['nurse_note', 'nurse_name','date', 'id', 'mrn']

    