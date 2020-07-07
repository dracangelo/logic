from django.db import models

# Create your models here.

class Service(models.Model):
    image = models.ImageField(upload_to='service/')
    title = models.CharField(max_length= 50)
    content = models.CharField(max_length= 50)


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title