from django.db import models

# Create your models here.
class busses(models.Model):
    origin=models.CharField(max_lenght=30)
    destination=models.CharField(max_lenght=30)
    duration=models.IntegerField()
