from django.contrib import admin

# Register your models here.
from .models import Bus,Station
admin.site.register(Bus)
admin.site.register(Station)

