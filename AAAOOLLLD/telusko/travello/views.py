from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(request): # when user request 

    # dest1 = Destination()
    # dest1.name = "Ogun"
    # dest1.img = "1.png"
    # dest1.desc = "Gateway state"
    # dest1.price = 700
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "Lagos"
    # dest2.img = "2.png"
    # dest2.desc = "Center of Excellence state"
    # dest2.price = 450
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Ekiti"
    # dest3.img = "3.png"
    # dest3.desc = "My gee state"
    # dest3.price = 450
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]


    dests = Destination.objects.all()

    # return HttpResponse("<h1>hello word</h1>") # then the get a repnse
    return render(request, 'index.html', {'dests':dests}) 
