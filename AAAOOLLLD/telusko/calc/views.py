from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request): # when user request 
    # return HttpResponse("<h1>hello word</h1>") # then the get a repnse
    return render(request, 'home.html', {'name':'Fatherhero'}) 

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request, "result.html", {"result": res}) 