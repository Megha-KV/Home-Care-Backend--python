from rest_framework import serializers
from .models import GeneralDetails



class GeneralDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDetails
        fields = '__all__'