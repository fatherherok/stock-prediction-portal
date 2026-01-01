from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


# Create your views here.
# def main(request):
#     return HttpResponse("<h1>hello</h1>")

class RoomView(generics.ListCreateAPIView):

# class RoomView(generics.CreateAPIView): #allow us to View all rooms row and Create a new room row
    queryset = Room.objects.all() #to view all the rooms
    serializer_class = RoomSerializer #after view all the rows, we can now put all the fields of the rooms with the seralizer



