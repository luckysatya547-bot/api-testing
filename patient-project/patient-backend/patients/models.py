from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Required fields
    patient_name  = models.CharField(max_length=200)
    gender        = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number  = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    state         = models.CharField(max_length=100)
    locality      = models.CharField(max_length=200)
    pincode       = models.CharField(max_length=10)

    # Optional fields
    email         = models.EmailField(blank=True, null=True)
    address       = models.TextField(blank=True, null=True)
    city          = models.CharField(max_length=100, blank=True, null=True)
    aadhaar_no    = models.CharField(max_length=20, blank=True, null=True)
    height        = models.CharField(max_length=10, blank=True, null=True)
    weight        = models.CharField(max_length=10, blank=True, null=True)

    # Auto fields
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name