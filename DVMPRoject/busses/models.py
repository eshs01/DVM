from django.db import models

# Create your models here.
class STATION(models.Model):
    code=models.CharField(max_length=6)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
class BUSSES(models.Model):
    origin = models.ForeignKey(STATION,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(STATION,on_delete=models.CASCADE,related_name="arivals")
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.id}:{self.origin} {self.destination}"
class Passanger(models.Model):
    name=models.CharField(max_length=80)
    busses=models.ManyToManyField(BUSSES,blank=True,related_name="passanger")
    def __str__(self):
        return f"{self.name}"