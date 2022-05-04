
from calendar import c
import email
from email import message
import re
from unicodedata import name
from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from home.models import Contact,Fee,Player, Trainer
from django.contrib import messages

# Create your views here.

def index(request):
    
    # return HttpResponse("This is index page")
    
    return render(request,'index.html')

def about(request):
    # return HttpResponse("This is about section")
    return render(request,'about.html')

def player(request):

     if request.method== "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone=request.POST.get('phone')
        profession=request.POST.get('profession')
        message= request.POST.get('message')

        player=Player(name=name,email=email,phone=phone,profession=profession,message=message,date=datetime.today())
        player.save()
    
        messages.success(request, 'The message has been sent.')
    # return HttpResponse("This is player ")
     return render(request,'player.html')

def trainer(request):

    if request.method== "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone=request.POST.get('phone')
        expert=request.POST.get('expert')
        message= request.POST.get('message')

        trainer=Trainer(name=name,email=email,phone=phone,expert=expert,message=message,date=datetime.today())
        trainer.save()
    
        messages.success(request, 'The message has been sent.')
    # return HttpResponse("This is trainer")
    return render(request,'trainer.html')

def fee(request):
    # return HttpResponse("This is fees")

    if request.method== "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        amount=request.POST.get('amount')
        message=request.POST.get('message')
        
        fee=Fee(name=name,email=email,phone=phone,Amount=amount,message=message,date=datetime.today())
        fee.save()
        messages.success(request, 'The message has been sent.')
        
    return render(request,'fee.html')

def contact(request):
    if request.method== "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        
        contact =Contact(name=name, email=email,message=message,date=datetime.today())
        contact.save()

        messages.success(request, 'The message has been sent.')

        
    return render(request,'contact.html')



def login(request):
    

    return render(request,'login.html')
    
    
    
    

   

    