from django.shortcuts import render
from .models import contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')    

def CONTACT(request):
    if request.method=='POST':
        contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_number=request.POST['contact_number']
        contact_message=request.POST['contact_message']

        Contact = contact(contact_name=contact_name,contact_email=contact_email,contact_number=contact_number,contact_message=contact_message)
        Contact.save()

    return render(request,'contact.html')          

def news(request):
    return render(request,'news.html')  

def mission(request):
    return render(request,'mission.html')      

def donate(request):
    return render(request,'donate.html')  

