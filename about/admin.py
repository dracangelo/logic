from django.contrib import admin
from .models import Aboutus, Testimonial, Team, Reservation

# Register your models here.

admin.site.register(Aboutus)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Reservation)