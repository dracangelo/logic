from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse  , HttpResponseRedirect
from .forms import ContactForm
from .models import Contact

# Create your views here.


def send_email(request):    
    contact = Contact.objects.last()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']

            try : 
                send_mail(subject,message,from_email,['admin@example.com'])

            except BadHeaderError:
                return HttpResponse('invalid header') 

            return redirect('contact:send_success')
    

    else:
        form = ContactForm()

    context = {
        'form' : form,
        'contact':contact,
    }

    return render(request , 'contact/contact.html' , context)



def send_success(request):
    return HttpResponse('thanks you for you email ^_^')