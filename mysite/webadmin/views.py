from django.shortcuts import render

from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from datetime import datetime, timedelta
import json
import hashlib

class Timeperiod(forms.Form):
    start = forms.DateField(label="Start", required=True)
    end = forms.DateField(label="End", required=True, )

class NewUser(forms.Form):
    name = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    email = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    password = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    teams = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))


def index (request):             

    return render(request, "webadmin/index.html",{      
    })

def users (request): 
    

    class historyInstance:
        def __init__(self, user, embedded,timestamp):
            self.user = user
            self.embedded = embedded
            self.timestamp = timestamp

    userHistory = []

    time = datetime.now().strftime('%H:%M') 


    userHistory.append(historyInstance("Kronborg","Mødelokale 1", time))   
    userHistory.append(historyInstance("Kronborg","Mødelokale 1", time))   
    userHistory.append(historyInstance("Kronborg","Mødelokale 1", time))   
    userHistory.append(historyInstance("Kronborg","Mødelokale 1", time))   
    userHistory.append(historyInstance("Kronborg","Mødelokale 1", time))   
    userHistory.append(historyInstance("Kronborg","Mødelokale 1", time)) 

    if request.method == "POST":

        #HHis man har sat en dato
        timeperiodForm = Timeperiod(request.POST)
        newUser = NewUser(request.POST)

        if newUser.is_valid():


            name = newUser.cleaned_data["name"]
            email = newUser.cleaned_data["email"]
            password = newUser.cleaned_data["password"]
            teams = newUser.cleaned_data["teams"]
            print(teams)


        if timeperiodForm.is_valid():

            start = timeperiodForm.cleaned_data["start"]
            end = timeperiodForm.cleaned_data["end"]

        return render(request, "webadmin/users.html",{  

        "history" : userHistory,      
        
    })
   

    return render(request, "webadmin/users.html",{  


        "history" : userHistory
        
    } )


def rooms (request):
    return render(request, "webadmin/rooms.html",{

    })


def login(request):

    email = ""
    password = ""

    if request.method == "POST":

        email = request.POST["email_test"]
        password = request.POST["password"]

        # myobj = {'email': email, "password": password}
        # x = requests.post(url + "auth/adminlogin", json=myobj)
        # json_response = x.json()

        # token = json_response["token"]

        # session = requests.session()
        # request.session['token'] = token

        # return HttpResponseRedirect(reverse("index"))

    return render(request, "webadmin/login.html",{
        "email" : email,
        "password" : password
        
    })