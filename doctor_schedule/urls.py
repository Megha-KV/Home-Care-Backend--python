from django.urls import path
from . import views



urlpatterns = [
    path('doctorschedule/', views.DoctorScheduleView.as_view()),
    path('doctorappointment/',views.GetScheduleDoctor.as_view()),
    path('doctorconflict/',views.CheckScheduleConflict.as_view())
    ]