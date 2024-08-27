from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.Patient.as_view()),
    path('patient-data/', views.GetDataAPIView.as_view()),

    ]