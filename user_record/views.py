from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRecordSerializer
from .models import appuser
from djongo.database import DatabaseError
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from datetime import datetime



class UserRecordView(APIView):
    permission_classes = [IsAuthenticated]
    model = appuser
    Model_serializer = UserRecordSerializer
    
    def post(self, request):
        try:
            print(request.data)
            item_serializer = self.Model_serializer(data=request.data)
            if item_serializer.is_valid():
                item_serializer.save()
                return Response(item_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        if request.query_params:
            items = self.model.objects.filter(**request.query_params.dict())
        else:
            items = self.model.objects.all().exclude(role = 'Admin')
        
        serializer = self.Model_serializer(items, many=True)
        return Response(serializer.data)

        


    def patch(self, request):
        item = self.model.objects.filter(user_id=request.data.get('user_id')).first()
    
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.Model_serializer(item, data=request.data, partial=True)
    
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        item =self.model.objects.filter(user_id=request.data.get('user_id')).first()
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserLogout(APIView):
    def get(self, request):
        if 'username' in request.session:
            try:
                # Delete the user's token to logout
                request.session.flush()
                return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'Already logged out.'}, status=status.HTTP_400_BAD_REQUEST)



User = get_user_model()

class ResetPassword(APIView):
    def post(self, request):
        if request.method == 'POST':
            email = request.session.get('email')
            if not email:
                return JsonResponse({'error': 'Email not found in session'}, status=status.HTTP_400_BAD_REQUEST)
            
            new_password = request.data.get('new_password')

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'error': f'User with email "{email}" does not exist'}, status=status.HTTP_404_NOT_FOUND)

            # Update the user's password
            user.set_password(new_password)
            user.save()

            return JsonResponse({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)

        return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





def generate_otp(length=6):
    """
    Generate a random OTP of the specified length.
    """
    digits = [str(random.randint(0, 9)) for _ in range(length)]
    return ''.join(digits)


@api_view(['POST'])
def forgot_password(request):
    if request.method == 'POST':
        email = request.data.get('email')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': f'User with email "{email}" does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Generate OTP
        otp = generate_otp()
        print(settings.DEFAULT_FROM_EMAIL)
        user.otp = otp
        user.save()
        # Send email to the user with the OTP for verification
        send_mail(
            subject="Home Care App OTP Verification",
            message=f"Your OTP is: {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,  # Use settings.DEFAULT_FROM_EMAIL
            recipient_list=[email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'OTP has been sent to your email.'}, status=status.HTTP_200_OK)

    return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['POST'])
def reset_password_confirm(request):
    if request.method == 'POST':
        email = request.data.get('email')
        otp_entered = request.data.get('otp')
        new_password = request.data.get('new_password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the OTP matches the one sent to the user
        # Replace the condition with your OTP verification logic
        if otp_entered == user.otp:
            # Reset the user's password
            user.set_password(new_password)
            user.save()
            return JsonResponse({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserLogin(APIView):
    def post(self, request):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            print(email,password)
            print(request.data)

            try:
                user = appuser.objects.get(email=email)
            except appuser.DoesNotExist:
                return Response({'error': 'User with the email does not exist'}, status=status.HTTP_401_UNAUTHORIZED)

            checked = check_password(password, encoded=user.password)
            if checked:
                Refresh_token = RefreshToken.for_user(user)
                access_token = Refresh_token.access_token
                 # Update last login date and time
                # user.last_login = datetime.now()
                user.save()
                request.session['email'] = user.email
                return Response({'message': 'Logged in','role':user.role,'refresh':str(Refresh_token),'access':str(access_token),'email' : user.email,'photo':user.photo.url,'username' : user.first_name + " "+ user.middle_name,'user_id':user.user_id} , status=status.HTTP_200_OK)
            
            return Response({'error': 'Password is wrong'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)