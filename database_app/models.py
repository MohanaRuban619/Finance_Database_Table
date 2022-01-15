from django.db import models

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
    Person_Photo = models.ImageField(upload_to='pics')
    Pic_promissory_note = models.ImageField(upload_to='pics')
    Pic_Id_Proof = models.ImageField(upload_to='pics')
    pic_Cheque = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Name
# Create your models here.
