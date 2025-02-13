from django.urls import path
from .import views
urlpatterns =[
    path("",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="logout"),
    path("home",views.home,name="home"),
    path("<int:bus_id>/",views.details,name="bus"),
    path("bookinghistory",views.bookinghistory,name="book")
    
   


]