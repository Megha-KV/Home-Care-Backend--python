from djongo import models

class GeneralDetails(models.Model):
    op_no = models.IntegerField()
    first_name = models.CharField(max_length= 50 , null = True , blank=True)
    age =models.CharField(max_length = 50 ,null = True , blank=True)
    sex = models.CharField(max_length = 50 ,null = True , blank=True)
    full_name= models.CharField(max_length = 50, null = True , blank=True)
    ref_clinician = models.CharField(max_length =50,null = True , blank=True)
    privacy_mode = models.CharField(max_length = 50,null = True , blank=True)


    general_appearance = models.CharField(max_length=200,null = True , blank=True)
    vital_signs = models.CharField(max_length=200,null = True , blank=True)
    other_signs = models.CharField(max_length=200,null = True , blank=True)

    ears_examination = models.CharField(max_length=50,null = True , blank=True)
    nose_examination = models.CharField(max_length=50,null = True , blank=True)
    throat_examination = models.CharField(max_length=50,null = True , blank=True)
    face_examination = models.CharField(max_length=50,null = True , blank=True)
    neck_examination = models.CharField(max_length=50,null = True , blank=True)

    
    def __str__(self):
        return str(self.op_no)