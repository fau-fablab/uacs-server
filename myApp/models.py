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
    
    Laser_last_use = models.DateField(auto_now = True) # 
    Laser_strikes = models.TextField(default = '') # Can be used to log dates the rules were violated
    Fraese_last_use = models.DateField(auto_now = True)
    Fraese_strikes = models.TextField(default = '')
    

    def __str__(self):
        return str(self.id)


class fablabDevice(models.Model):
    Name = models.CharField(max_length=20, default="defaultdevice")
	
    userruntime = models.IntegerField()
    betreuerruntime = models.IntegerField()
    active = models.BooleanField()
    def __str__(self):
        return str(self.Name)
# Create your models here.
