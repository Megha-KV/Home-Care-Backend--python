from django.urls import path
from . import views
urlpatterns = [
    path('vitals/', views.PatientVital.as_view()),
    path('get-data/', views.GetVitalSign.as_view())
    ]