from django.db import models


class fablabUser(models.Model):

    fauid = models.CharField(max_length=10, default="faudauid")
    cardid = models.CharField(max_length=15, default="00000")
    Name = models.CharField(max_length=200, default='fablabdau')
    Betreuer = models.BooleanField(default = False)
    Fraese = models.BooleanField(default = False)
    Laser = models.BooleanField(default = False)
    Fernbedienung = models.BooleanField(default = False)
    Kabelbinder = models.BooleanField(default = False)

    def __str__(self):
        return str(self.id)


class fablabDevice(models.Model):

    Name = models.CharField(max_length=20, default="laser")
    runtime = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return str(self.Name)
# Create your models here.
