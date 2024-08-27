from djongo import models

# Create your models here.
class Entry(models.Model):
    # nurse_id = models.CharField(max_length = 50)
    nurse_note = models.TextField()
    nurse_name = models.CharField(max_length=100)
    date = models.DateTimeField( auto_now=False, auto_now_add=True)
    mrn = models.CharField(max_length=50)
    
