from djongo import models

class Patientregistration(models.Model):
    File_no = models.CharField(max_length=50)
    mr_no = models.CharField(max_length=50)
    consult_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    dept = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    clinician = models.CharField(max_length=50)
    ord_clinician = models.CharField(max_length=50)
    ref_clinician = models.CharField(max_length=50)
    diag_clinic = models.CharField(max_length=50)
    diag_clinician = models.CharField(max_length=50)
   
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    emirated_id = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    passport_id = models.CharField(max_length=50)
    unified = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')


    full_name = models.CharField(max_length = 50)
    relationship = models.CharField(max_length = 50 )
    contact = models.CharField(max_length = 50)




    address = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    resi_of_emirates = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    work_no = models.CharField(max_length=20)
    email = models.EmailField()


    company = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    membership_id = models.CharField(max_length=50)
    additional_info = models.TextField()
    issue_date = models.DateField()
    expiry_date = models.DateField()
    eligibility_id = models.CharField(max_length=50)
    payer_id = models.CharField(max_length=50)

    def _str_(self):
        return f"MR No: {self.mr_no}, Consult ID: {self.consult_id}"
    
    '''def save(self, *args, **kwargs):
        if not self.consult_id:
            # Get the last consult_id from the database
            last_patient = Patientregistration.objects.order_by('-consult_id').first()
            last_consult_id = int(last_patient.consult_id) if last_patient else 99
            
            # Increment the last consult_id by 1
            new_consult_id = str(last_consult_id + 1)
            
            self.consult_id = new_consult_id.zfill(3)  # Zero-fill the consult_id
        
        super(Patientregistration, self).save(args,*kwargs)'''