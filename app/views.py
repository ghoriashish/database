from django.shortcuts import render,HttpResponseRedirect,reverse
from . models import *
# Create your views here.
def  Indexpage(request):
    return render(request,"app/index.html")
def  sucess(request):
    return render(request,"app/sucess.html")



def registeruser(request):
   
    firstname=request.POST['fname']
    lastname=request.POST['lname'] 
    email=request.POST['email']
    image=request.FILES['image']   
    newuser=user.objects.create(Firstname=firstname,Lastname=lastname,Email=email,profile_pic=image)
    return HttpResponseRedirect(reverse("alldetail1"))


def alldetail(request):
    alluser=user.objects.all()    
    return render(request,"app/sucess.html",{'key':alluser})