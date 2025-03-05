from django.shortcuts import render
from django.http import HttpResponse


# home page
def home(request):
    context_dict={}
    return render(request, 'hikit/home.html', context = context_dict)
    
# events page
def events(request):
    context_dict={}
    return render(request, 'hikit/events.html', context = context_dict)

# myprofile page
def myprofile(request):
    context_dict={}
    return render(request, 'hikit/myprofile.html', context = context_dict)

# editpost page
def editpost(request):
    context_dict={}
    return render(request, 'hikit/editpost.html', context = context_dict)

# login page
def login(request):
    context_dict={}
    return render(request, 'hikit/login.html', context = context_dict)
