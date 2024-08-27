from rest_framework import serializers
from .models import appuser
from django.contrib.auth.hashers import make_password
from drf_extra_fields.fields import Base64ImageField


class UserRecordSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()
    class Meta:
        model = appuser
        fields =['first_name','middle_name','last_name','job','role','type_mode','license','validity','user_id','password','cs_allow','session_exp','email','mf_no','creation_date','photo']
        extra_kwargs ={
            'password' : {'write_only' : True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = appuser.objects.create(**validated_data)
        user.password = make_password(password)
        user.is_active = True
        user.save()
        return user
