from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    services = Service.objects.all()

    context = {
        'service':services 
    }

    return render(request, 'service/services.html', context)