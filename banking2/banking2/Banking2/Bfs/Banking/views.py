from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Register

def homepage(request):
    return render(request,"Banking/homepage.html")
def login(request):
    return render(request,"Banking/login.html")
def register(request):
    return render(request,"Banking/register.html")
def addRegister(request):
    if request.method=='POST':
        fullname=request.POST["fname"]
        username = request.POST["uname"]
        email = request.POST["email"]
        mobileno = request.POST["mobile"]
        password=request.POST["pwd"]
        cpassword=request.POST["cpwd"]
        account = request.POST["account"]
        gender=request.POST["gender"]
        flag=Register.objects.create(fullname=fullname,username=username,email=email,mobileno=mobileno,password=password,cpassword=cpassword,account=account,gender=gender)
        if flag:
            return render(request,'Banking/registers.html')
        else:
            return HttpResponse("Invalid credentials")
        return HttpResponse("Invalid Details!")
def checklogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        flag=Register.objects.filter( Q(username__iexact=username) & Q(password__iexact=password) )
        if flag:
            return HttpResponse("Valid User Login")
        else:
            return HttpResponse("Invalid User Login")
    else:
        return HttpResponse("Failed Login")
# Create your views here.
