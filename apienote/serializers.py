from rest_framework import serializers
from .models import ApieNote

class ApieNursingSerializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only = True)
    nurse_name = serializers.CharField(read_only = True)
    date = serializers.DateTimeField(read_only = True)
    
    class Meta:
        model = ApieNote 
        fields = ['nurse_name','date','assessment','planning','intervention','evaluation','id','mrn']
        