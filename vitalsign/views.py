from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VitalSerializer
from .models import PatientVitalSign


class PatientVital(APIView):
    model = PatientVitalSign
    Model_serializer = VitalSerializer
    def get(self, request):
        if request.query_params:
            items = self.model.objects.filter(**request.query_params.dict())
        else:
            items = self.model.objects.all()
            
        serializer =  self.Model_serializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        item_serializer = self.Model_serializer(data=request.data)

        # Validate for already existing data
        if self.model.objects.filter(**request.data).exists():
            return Response({'error': 'This data already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if item_serializer.is_valid(raise_exception=True):
            item_serializer.save()
            return Response(item_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        item =self.model.objects.filter(id=request.data.get('id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer =  self.Model_serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        item =self.model.objects.filter(id=request.data.get('id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GetVitalSign(APIView):
    def get(self, request):
        mrn = request.query_params.get('mrn')
        try:
            item = PatientVitalSign.objects.filter(mrn=mrn).latest('created_time')
            if item:
                serializer = VitalSerializer(item)
                return Response(serializer.data)
            else:
                return Response({'error': 'Patient with provided MRN not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle database errors
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)