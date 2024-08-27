from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApieNursingSerializer
from .models import ApieNote
from django.db import DatabaseError
from user_record import models as userModels
from rest_framework.exceptions import ValidationError


class ApieNursingNote(APIView):
    model = ApieNote
    Model_serializer = ApieNursingSerializer
    def get(self, request):
        mrn = request.query_params.get('mrn')  # Assuming MRN is sent in the request body
        if mrn:
             items = self.model.objects.filter(mrn=mrn)
             serializer = self.Model_serializer(items, many=True)
             return Response(serializer.data)
        else:
            return Response({'error': 'MRN parameter is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)

   

    def post(self, request):
        try:
            email = request.user.email
            item_serializer = self.Model_serializer(data=request.data)
            nurse = userModels.appuser.objects.get(email = email)

            if item_serializer.is_valid():
                item_serializer.save(nurse_name = str(nurse.first_name)+" "+str(nurse.middle_name))
                return Response(item_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except DatabaseError as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        item =self.model.objects.filter(id=request.data.get('id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer =  self.Model_serializer(item, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        item =self.model.objects.filter(id=request.data.get('id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        serializer = self.Model_serializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)


class GetApieNote(APIView):
    def get(self, request):
        id= request.query_params.get('id')
        if id:
            try:
                item = ApieNote.objects.get(id=id)
                serializer = ApieNursingSerializer(item)
                return Response(serializer.data)
            except ApieNote.DoesNotExist:
                return Response({'error': 'Patient with provided ID not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            raise ValidationError({'error': 'ID parameter is required'})