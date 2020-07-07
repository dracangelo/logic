from django.db import models

# Create your models here.

freight = (
    ('Less Than Truckload' , "Less Than Truckload"),
    ('Truckload' , "Truckload"),
    ('Intermodal' , "Intermodal"),
    ('Expedited' , "Expedited")
)

class Reservation(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.IntegerField()
    cityofdeparture = models.CharField(max_length=70)
    incoterms = models.CharField(max_length=70)
    weight_kg = models.IntegerField()
    height_m = models.IntegerField()
    length_m = models.IntegerField()
    freight = models.CharField(choices=freight, max_length=10)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name

class Aboutus(models.Model):
    title = models.CharField(max_length= 50)
    subtitle = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

    def __str__(self):
        return self.title
        


class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    title = models.CharField(max_length= 50)
    position = models.CharField(max_length= 50)


    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length= 50, default=True)
    content = models.TextField()
    client = models.CharField(max_length= 50)
    image = models.ImageField(upload_to='testimonial/')    
    occupation = models.CharField(max_length= 50)


    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.title
