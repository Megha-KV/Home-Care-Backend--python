from djongo import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator



class AppUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(email=username)
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role','Admin')
        extra_fields.setdefault('photo','photos/2b0f192c-950f-40eb-b7fa-65017cf236aa.jpg')


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class appuser(models.Model):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
        ('Nurse', 'Nurse'),
    ]
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,null = True,blank = True)
    type_mode = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    validity = models.DateField()
    user_id = models.CharField(max_length=50 , unique=True)
    password = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r'^[a-zA-Z0-9]*$',
        message='Password must contain only letters and numbers',
    )])
    cs_allow = models.CharField(max_length=50)
    session_exp = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    mf_no = models.CharField(max_length=50)
    creation_date = models.DateField()
    photo = models.ImageField(upload_to='photos')
    otp = models.CharField(max_length=50, null=True, blank=True)

    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = AppUserManager()

    def set_password(self, raw_password):
        """
        Set the password for the user.

        Args:
            raw_password (str): The raw password string.
        """
        self.password = make_password(raw_password)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_authenticated(self):
        return True  # Assuming all instances of UserRecord are authenticated

    @property
    def is_anonymous(self):
        return False  # Assuming all instances of UserRecord are not anonymous