from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api/',include('patientregistration.urls')),
    path('api/',include('vitalsign.urls')),
    path('api/',include('user_record.urls')),
    path('api/',include('patiententry.urls')),
    path('api/',include('apienote.urls')),
    path('api/',include('clinical_evaluation.urls')),
    path('api/',include('nurse_schedule.urls')),
    path('api/',include('doctor_schedule.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
