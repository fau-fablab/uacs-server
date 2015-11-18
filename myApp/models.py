from django.db import models

class fablabUser(models.Model):

	fauid = models.CharField(max_length=10, default="faudauid")
	cardid = models.CharField(max_length=15, default="00000")
	Name = models.CharField(max_length=200, default='fablabdau')
	Betreuer = models.BooleanField()
	Fraese = models.BooleanField()
	Laser = models.BooleanField()
	Fernbedienung = models.BooleanField()
	Kabelbinder = models.BooleanField()
	def __str__(self):
		return str(self.fauid)

# Create your models here.
