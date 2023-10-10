from django.shortcuts import render

from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from datetime import datetime, timedelta
import json
import hashlib
import requests



class Timeperiod(forms.Form):
    start = forms.DateField(label="Start", required=True)
    end = forms.DateField(label="End", required=True, )

class NewUser(forms.Form):
    name = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    email = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    password = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    code = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))
    teams = forms.CharField(label="password", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))


class DeleteUser(forms.Form):
     id = forms.CharField(label="id", required=True, widget=forms.TextInput(attrs={'placeholder': 'Beskrivelser'}))

class User:
        def __init__(self, id,name, email,CreatedAt):
            self.id = id
            self.name = name
            self.email = email  
            self.CreatedAt = CreatedAt   

class Team:
        def __init__(self,id,name):
            self.id = id
            self.name = name

class historyInstance:
    def __init__(self, user, embedded, id, timestamp):
        self.user = user
        self.embedded = embedded
        self.id = id
        self.timestamp = timestamp


class Room:
        def __init__(self,id,name, timestamp):
            self.id = id
            self.name = name
            self.timestamp = timestamp

def NewPaginator(request,list, itemsPerPage, param):

    paginator = Paginator(list, itemsPerPage)   
    page_number = request.GET.get(param) 
    page = paginator.get_page(page_number)

    return page


time = datetime.now().strftime('%H:%M')  

api_url = "https://api.seaofkeys.com"

def GetAPI(endpoint):

    x = requests.get(api_url + endpoint)
    return x    

def PostAPI(endpoint, obj):
    x = requests.post(api_url + endpoint,obj)
    return x

def index (request):
    
    if request.session.get("token") == None:            
            return redirect("/login")    

    usersTotal = 10
    roomsTotal = 33

    class Users:
        def __init__(self,usersX,usersY):
            self.usersX = usersX
            self.usersY = usersY

    usersX = ["24-09-2023", "25-09-2023","26-09-2023", "27-09-2023", "28-09-2023","29-09-2023","30-09-2023"]
    usersY = ["20","21","24","30","32","35","40"]   

    users = Users(usersX,usersY)


    return render(request, "webadmin/index.html",{    
        "usersTotal" : usersTotal,
        "roomsTotal" : roomsTotal,
        "users" : users,     
        
          
    })

def users (request):    

    if request.session.get("token") == None:            
            return redirect("/login")   

    userHistory = []

    time = datetime.now().strftime('%H:%M')      

    url =  api_url + "/user"
    x = requests.get(url)
    json_response = x.json()  

    for x in range(100):      
        userHistory.append(historyInstance("Kronborg","Mødelokale 1",x, time))   

    user_page = NewPaginator(request,json_response,5,"userPage")
    history_page = NewPaginator(request,userHistory,9,"historyPage")

    
    if request.method == "POST":

        #Hvis man har sat en dato
        timeperiodForm = Timeperiod(request.POST)
        newUser = NewUser(request.POST)

        if newUser.is_valid():

            name = newUser.cleaned_data["name"]
            email = newUser.cleaned_data["email"]
            password = newUser.cleaned_data["password"]
            code = newUser.cleaned_data["code"]
            teams = newUser.cleaned_data["teams"]

            url = "https://api.seaofkeys.com/user"
            myobj = {"name" : name, 'email': email, "password": password, "code" : code}           
            x = requests.post(url, json=myobj)
            json_response = x.json()   


            return HttpResponseRedirect(reverse("users"))
    

        if timeperiodForm.is_valid():

            start = timeperiodForm.cleaned_data["start"]
            end = timeperiodForm.cleaned_data["end"]

   
    return render(request, "webadmin/users.html",{  


        "history" : userHistory,        
        "userPage" : user_page,
        "historyPage" : history_page
        
    })


def deleteMultiple(request,endpoint):     

    if request.method == "POST":         

        id = request.POST["id"]
        id = id.split(",")

        ids = list()

        for item in id:
             
             if item != "":
                  
                  ids.append({ "id": int(item) })
        
        url = api_url + endpoint          
        x = requests.delete(url, json=ids)       

def deleteuser(request):
        
    deleteMultiple(request,"/user/del/")
    return HttpResponseRedirect(reverse("users"))

def edituser(request):
     
    if request.method == "POST":          

        id = request.POST["id"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        code = request.POST["code"]

        url = "https://api.seaofkeys.com/user"
        myobj = {"id" : int(id), "name" : name, 'email': email, "password": password, "code" : code} 
    
        x = requests.put(url, json=myobj)
        json_response = x.json()   

    return HttpResponseRedirect(reverse("users"))    
          

def user(request,id):

    if request.session.get("token") == None:            
            return redirect("/login")   

    time = datetime.now().strftime("%H:%M %D")
    currentUser = User(id,"Morten","bindzus@mail.dk",time) 
    teams = []

    userHistory = []

    for x in range(10):   
        userHistory.append(historyInstance("Kronborg","Mødelokale 1", x, time)) 

    for x in range(5):
        teams.append(Team(x,"Kantinedamerne"))

    #Pagination
    team_page = NewPaginator(request,teams,3,"teamPage")
    history_page = NewPaginator(request,userHistory,3,"userHistory")

    return render(request, "webadmin/user.html",{
        "user" : currentUser,
        "teams" : teams,
        "history": userHistory,
        "teamPage" : team_page,
        "historyPage" : history_page
    })


def rooms (request):

    if request.session.get("token") == None:            
            return redirect("/login")   


    rooms = []

    time = datetime.now().strftime("%H:%M %D")
    for x in range(27):   
        rooms.append(Room(x,"Mødelokale 1", time))

    
    roomsPage = NewPaginator(request,rooms,5,"roomsPage")


    return render(request, "webadmin/rooms.html",{

        "roomsPage" : roomsPage

    })

def room(request,id):

    if request.session.get("token") == None:            
            return redirect("/login")   


    teams = []
    history = []
    time = datetime.now().strftime("%H:%M %D")    
    room = Room(1,"Mødelokale",time)

    for x in range(23):
        teams.append(Team(x,"Kantinedamerne"))      
        history.append(historyInstance("Bruger","Dør 1",x,time))

    teamRoomsPage = NewPaginator(request,teams,5,"teamRoomsPage")
    historyPage = NewPaginator(request,history,5,"historyPage")


    return render(request, "webadmin/room.html",{

        "room" : room,
        "teams" : teams,
        "teamRoomsPage" : teamRoomsPage,
        "historyPage" : historyPage
    })

def teams(request):

    if request.session.get("token") == None:            
            return redirect("/login")   

    users = GetAPI("/user").json()
    teams = GetAPI("/team").json()["team"]  
    teamsPage = NewPaginator(request,teams,6,"teamsPage")



    if request.method == "POST":
         
        name = request.POST["name"]   
        newUsers = request.POST["users"].split(",")       
        
        userObj = list()       
        
        for item in newUsers:
            
            userObj.append({"id" : int(item)})                
        
        obj = {"name" : name, "users" : userObj}        
        
        
        print(obj)
        
        statuscode = PostAPI("/team",obj).status_code

        print(statuscode)

        return HttpResponseRedirect(reverse("teams"))    
        

    return render(request, "webadmin/teams.html",{

        "teamsPage" : teamsPage,
        "users": users,

    })


def deleteteam(request):
     
    deleteMultiple(request,"/team/del")  
    return HttpResponseRedirect(reverse("teams"))   

def editteam(request):   
     
    if request.method == "POST":          

        id = request.POST["id"]
        name = request.POST["name"]         

        url = api_url + "/team"
       
        myobj = {"id" : int(id), "name" : name} 
    
        x = requests.put(url, json=myobj)
        json_response = x.json()   
    
    return HttpResponseRedirect(reverse("teams"))     

def team(request,id):

    if request.session.get("token") == None:            
            return redirect("/login")   

    users = []
    team = Team(1,"Køkkendamerne")


    for x in range(25):

        users.append(User(x,"Morten","morten@mail.dk",time))

    teamUsersPage = NewPaginator(request,users,5,"teamUsersPage")

    return render(request, "webadmin/team.html",{

        "teamUsersPage" : teamUsersPage,
        "team" : team,
        "users" : users,       

    })


def login(request):    

    email = ""
    password = ""

    if request.method == "POST":

        email = request.POST["email_test"]
        password = request.POST["password"]


        email = "mkronborg7@gmail.com"
        password = "Test"

        url = "https://api.seaofkeys.com/auth/login"

        myobj = {'email': email, "password": password}
        x = requests.post(url, json=myobj)
        json_response = x.json()     

        token = json_response["token"]

        session = requests.session()
        request.session['token'] = token

        return HttpResponseRedirect(reverse("index"))

    return render(request, "webadmin/login.html",{
        "email" : email,
        "password" : password
        
    })

def logout(request):

    request.session['token'] = None
    
    return HttpResponseRedirect(reverse("login"))