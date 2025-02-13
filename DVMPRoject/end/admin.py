from django.contrib import admin

# Register your models here.
from .models import Bus,Station,Searchbus
admin.site.register(Bus)
admin.site.register(Station)
admin.site.register(Searchbus)


