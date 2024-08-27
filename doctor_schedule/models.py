from djongo import models
from django.core.exceptions import ValidationError

# Create your models here.
class DoctorSchedule(models.Model):
    doctor_id=models.CharField(max_length = 50)
    mr_no = models.CharField(max_length=50) 
    patient_name = models.CharField(max_length = 100)
    start_date =  models.DateField()
    end_date= models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.CharField(max_length= 100)
    photo = models.ImageField(upload_to='photos')
    consult_id = models.CharField(max_length=50)