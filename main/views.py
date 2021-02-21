from django.shortcuts import render
from django.http import HttpResponse
from .models import customer,transfer
from .forms import createForm
# Create your views here.

def index(response):
    return HttpResponse("hekllo")


def home(response):
    if response.method=="POST":
        form=createForm(response.POST)
        if form.is_valid():
            fc = form.cleaned_data["fromc"]
            n= form.cleaned_data["name"]
            am= form.cleaned_data["amount"]
            f = customer.objects.get(id=fc)
            t= customer.objects.get(id=n)
            customer.objects.filter(name=f.name).update(balance=f.balance-am)
            customer.objects.filter(name=t.name).update(balance=t.balance+am)
            j=transfer(fromName=f.name,toName=t.name,amount=am)
            j.save()
            
           
            
                  
    else:
        form= createForm()
    ts=transfer.objects.all()
    ls= customer.objects.all()
    return render(response,"main/home.html", {"form" : form, "ls":ls,"ts":ts})
