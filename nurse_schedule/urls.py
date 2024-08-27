from django.urls import path
from . import views




urlpatterns = [
    path('nurseschedule/', views.Schedule.as_view()),
    path('appointment/',views.GetSchedule.as_view()),
    path('nurseconflict/',views.CheckScheduleConflict.as_view()),
    ]