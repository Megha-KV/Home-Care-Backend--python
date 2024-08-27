from rest_framework import serializers
from .models import PatientVitalSign

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVitalSign
        fields = ['cid','mrn','infant','height','weight','bmi','rbs','fbs','o2_saturation','head_circum','chest_circum','waist_circum','hip_circum','abdo_circum','pain_score','temp_note','temp_site','pulse_note','pulse_site','respiration','bp_note']
        extra_kwargs = {
            'height': {'required': False}  # Set height field as not required by default
        }


    # def validate(self, data):
    #     infant = data.get('infant', False)
    #     height = data.get('height', '')

    #     if infant and height:
    #         raise serializers.ValidationError("Height cannot be entered for infants.")

    #     return data