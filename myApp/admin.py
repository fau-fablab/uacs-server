from django.contrib import admin

from .models import fablabUser
from .models import fablabDevice

admin.site.register(fablabUser)
admin.site.register(fablabDevice)



# Register your models here.
