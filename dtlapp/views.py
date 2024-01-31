from django.shortcuts import render
from datetime import datetime


# Create your views here.
# def index(req):
#     username = input("enter username=")
#     context = {"username": username}
#     # return render(req, "index.html", {"username": username})
#     return render(req, "index.html", context)

def index(req):
    username = "admin"
    products =["mobile", "laptop", "PC", "keyboard"]
    movies = {"KGF": 5, "SALAAR": 4, "PUSHPA": 3}
    fruits_data = fruits()
    context ={
        "username": username, 
        "products": products, 
        "movies": movies,
        "fruits_data": fruits_data
        }
    return render(req, "index.html", context)

def fruits():
    fruitslist = ("grapes", "mango", "banana")
    return fruitslist

def login(req):
    username = input("Enter username = ")
    todaysdate = datetime.now()
    context = {"username": username, "todaysdate": todaysdate}
    return render(req, "login.html", context)

