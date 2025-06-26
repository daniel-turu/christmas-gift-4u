from django.contrib import admin

# Register your models here.
from .models import Gift_Name, Device
admin.site.register(Gift_Name)
admin.site.register(Device)