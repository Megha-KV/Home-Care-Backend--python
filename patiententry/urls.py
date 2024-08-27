from django.urls import path
from . import views

urlpatterns = [
    path('entry/', views.PatientEntry.as_view()),
    path('one-entry/',views.GetPatientEntry.as_view())
    ]
