from django.shortcuts import render
from contact.models import Contact


# Create your views here.

def home(request):
    contact = Contact.objects.all()

    context = {
        'contact' : contact ,
        
    }

    return render(request , 'home/index.html' , context)