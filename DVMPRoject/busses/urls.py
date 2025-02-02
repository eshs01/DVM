from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:bus_id>",views.buz,name="bus")
    
]