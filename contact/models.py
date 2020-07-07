from django.db import models

# Create your models here.

class Contact(models.Model):
    
    email = models.EmailField(null=True)
    name = models.CharField(max_length=15, default=True)
    number = models.CharField(max_length=15, default=True)    
    location = models.CharField(max_length=70, default=True)
    

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'