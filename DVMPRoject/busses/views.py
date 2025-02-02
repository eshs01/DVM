from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BUSSES


# Create your views here.
def index(request):
    return render(request,"busses/index.html",{
        "busses":BUSSES.objects.all()
    })
def buz(request,bus_id):
    bus=BUSSES.objects.get(id=bus_id)
    return render(request,"busses/view.html",{
        "buss":bus,
        "pass":bus.passanger.all()
    })

