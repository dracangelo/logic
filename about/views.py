from django.shortcuts import render
from .models import Team, Testimonial, Aboutus, Reservation
from .forms import ReserveForm

# Create your views here.

def aboutus_list(request):
    about = Aboutus.objects.last()
    testimonial = Testimonial.objects.all()
    team = Team.objects.all()
    reserve_form = ReserveForm()
    
    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    
    else:
        reserve_form = ReserveForm()

    context = {
        'about': about,
        'testimonial':testimonial,
        'team':team,
        'reserve_form': reserve_form,
    }

    return render (request, 'about/about.html', context)