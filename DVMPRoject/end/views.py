from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Bus,Book,Searchbus
from django.shortcuts import get_object_or_404
# Create your views here
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))


    """return render(request,"end/home.html",{
        "bus":Bus.objects.all(),
        "search":Searchbus.objects.all()
    })"""


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    bus = Bus.objects.all() 

    if request.method == "POST":
        search_query = request.POST.get("bus", "")
        if search_query:
            bus = bus.filter(
                boarding__city__icontains=search_query  
            ) | bus.filter(
                destination__city__icontains=search_query  
            )

    return render(request, "end/home.html", {
        "bus": bus
    })


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "end/login.html", {
                "message": "Invalid credentials",
            })


    return render(request, "end/login.html")


def logoutuser(request):
    logout(request)
    return render(request,"end/login.html",{
        "message":"logged out"
    })

    
def details(request,bus_id):
    #bus=Bus.objects.get(id=bus_id)
    #save the details of specific Bus in bus
    #return render(request,"end/bus.html",{
    #   "bus":bus
        #passing bus(line38) to html in form of bus 
       # i joined the book and and the detail function as both of them werer not working seperately
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    bus =  Bus.objects.get(id=bus_id)
    if request.method == "POST":
        # Get the number of seats requested
        bookseats = int(request.POST.get("bookseats", 0))
        
        
        if bus.availableseats:
            if bookseats > bus.availableseats:
                return render(request, "end/bus.html", {
                    "bus": bus,
                    "message": "Not that many seats available",
                })
        bus.availableseats -= bookseats
        bus.save()
        Book.objects.create(
            user=request.user,
            bus = bus,
            bookseats=bookseats
        )

        
        return render(request, "end/bus.html", {
            "bus": bus,
            "message": f"Thank you for booking {bookseats} seat(s).",
        })
    return render(request, "end/bus.html", {
        "bus": bus
        })
    
"""
def book(request, bus_id):
    if request.method == "POST":
        bookseats = request.POST.get("no_of_seats")
        if not bookseats:
            return render(request, "end/bus.html",{
                "message": "Invalid input"
            })
        
        bookseats=int(bookseats)

        bus=Bus.objects.get(id=bus_id)
        if bookseats > bus.availableseats:
            return render(request, "end/bus.html", {
                "message": "Not enough seats available"
            })

        bus.availableseats-= bookseats
        bus.save()
        
        return render(request,"end/bus.html",{
            "message":"thank u for booking"
        })
wanna ask why this does not work
"""
def bookinghistory(request):

    bookings = Book.objects.filter(user=request.user).order_by('-bookseats')
    
    return render(request, "end/book.html", {
        "bookings": bookings
    })
