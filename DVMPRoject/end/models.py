from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Station(models.Model):
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.city} ({self.code})"

class Bus(models.Model):
    boarding = models.ForeignKey(Station,on_delete=models.CASCADE,related_name="departure")
    destination = models.ForeignKey(Station,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()
    seats = models.IntegerField(default=25)
    availableseats = models.IntegerField(default=25)
    

class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="uzer")
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    bookseats=models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.bus.id} - {self.bookseats} seats"
class Searchbus(models.Model):
    origin = models.ForeignKey(Bus,on_delete=models.CASCADE,related_name="origin")
    endpoint = models.ForeignKey(Bus,on_delete=models.CASCADE,related_name="endpoint")
    
