from django.urls import path
from . import views

urlpatterns = [
    path('userrecord/', views.UserRecordView.as_view()),
    path('logout/', views.UserLogout.as_view()),
    path('resetpassword/',views.ResetPassword.as_view()),
    path('login/', views.UserLogin.as_view()),
   
   ]