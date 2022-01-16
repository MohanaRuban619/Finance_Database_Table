from django.db import models
from cloudinary.models import CloudinaryField
class Destination(models.Model):
    Name = models.CharField(max_length=100)
    Principal_Amount = models.CharField(max_length=11)
    Intrest_Rate = models.CharField(max_length=5)
    Given_Intrest = models.CharField(max_length=8)
    Given_Principle = models.CharField(max_length=11)
    Pending_Intrest = models.CharField(max_length=8)
    Balance_Principle_Amount = models.CharField(max_length=11)
    Case_N0 = models.CharField(max_length=50)
    Case_Type = models.CharField(max_length=10)
    Case_link = models.CharField(max_length=200)
    Person_Photo = CloudinaryField('Person_Photo')
    Pic_promissory_note = CloudinaryField('Pic_promissory_note')
    Pic_Id_Proof = CloudinaryField('Pic_Id_Proof')
    Pic_Cheque = CloudinaryField('Pic_Cheque')

    def __str__(self):
        return self.Name
# Create your models here.
