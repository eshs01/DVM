from django.contrib import admin

# Register your models here.
from .models import STATION,BUSSES,Passanger
admin.site.register(STATION)
admin.site.register(BUSSES)
admin.site.register(Passanger)