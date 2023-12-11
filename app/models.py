from django.db import models

# Create your models here.
class Country(models.Model):
    cid=models.IntegerField(primary_key=True)
    countryname=models.CharField(max_length=100)
    def __str__(self):
        return self.countryname
class Capital(models.Model):
    capid=models.IntegerField(primary_key=True)
    capitalname=models.CharField(max_length=100)
    cid=models.OneToOneField(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.capitalname