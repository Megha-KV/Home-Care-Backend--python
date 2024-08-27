from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GeneralDetailSerializer
from .models import GeneralDetails
from django.db import DatabaseError




class GeneralDetailsView(APIView):
    model = GeneralDetails
    Model_serializer = GeneralDetailSerializer
    def get(self, request):
        if request.query_params:
            items = self.model.objects.filter(**request.query_params.dict())
        else:
            items = self.model.objects.all()
            
        serializer =  self.Model_serializer(items, many=True)
        return Response(serializer.data)

   

    def post(self, request):
        try:
            item_serializer = self.Model_serializer(data=request.data)

            if item_serializer.is_valid():
                item_serializer.save()
                return Response(item_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except DatabaseError as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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