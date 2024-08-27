from djongo import models

# Create your models here.
class ApieNote(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    nurse_name = models.CharField(max_length = 100)
    assessment = models.CharField(max_length = 2000)
    planning = models.CharField(max_length = 2000)
    intervention = models.CharField(max_length = 2000)
    evaluation = models.CharField(max_length = 2000)
    mrn = models.CharField(max_length=50)