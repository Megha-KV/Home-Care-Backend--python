from djongo import models

class PatientVitalSign(models.Model):
  cid = models.CharField(max_length=255)
  mrn= models.CharField(max_length=255, null = True,blank= True)
  height = models.CharField(max_length=255)
  infant = models.BooleanField(default=False)
  weight = models.CharField(max_length=255)
  bmi = models.CharField(max_length=255)
  rbs = models.CharField(max_length=255)
  fbs = models.CharField(max_length=255)
  o2_saturation = models.CharField(max_length=255)
  head_circum = models.CharField(max_length=255)
  chest_circum = models.CharField(max_length=255)
  waist_circum = models.CharField(max_length=255)
  hip_circum = models.CharField(max_length=255)
  abdo_circum = models.CharField(max_length=255)
  pain_score = models.CharField(max_length=255)
  temp_note = models.CharField(max_length=255)
  temp_site = models.CharField(max_length=255)
  pulse_note = models.CharField(max_length=255)
  pulse_site = models.CharField(max_length=255)
  respiration = models.CharField(max_length=255)
  bp_note = models.CharField(max_length=255)
  bp_site = models.CharField(max_length=255)
  created_time = models.DateTimeField(auto_now=True,null=True)

  def __str__(self):
        return self.cid
    
   