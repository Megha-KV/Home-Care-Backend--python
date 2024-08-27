from djongo import models
from django.core.exceptions import ValidationError

# Create your models here.
class NurseSchedule(models.Model):
    nurse_id = models.CharField(max_length = 50)
    patient_name = models.CharField(max_length = 100)
    start_date =  models.DateField()
    end_date= models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.CharField(max_length= 100)
    photo = models.ImageField()
    mr_no = models.CharField(max_length=50) 
    role = models.CharField(max_length = 50)
    consult_id = models.CharField(max_length=50)