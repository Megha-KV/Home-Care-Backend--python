from django.urls import path
from . import views

urlpatterns = [
    path('apie/', views.ApieNursingNote.as_view()),
    path('one-apie/',views.GetApieNote.as_view())
    ]