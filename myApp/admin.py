from django.contrib import admin

from .models import fablabUser
from .models import fablabDevice

class fablabUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'fauid', 'cardid', 'Name', 'Betreuer')

class fablabDeviceAdmin(admin.ModelAdmin):
	list_display = ('Name', 'runtime', 'active')

admin.site.register(fablabUser, fablabUserAdmin)
admin.site.register(fablabDevice, fablabDeviceAdmin)

# taken from http://www.djangobook.com/en/2.0/chapter06.html	

# Register your models here.
