# Generated by Django 2.2.7 on 2020-06-30 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20200630_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='title',
        ),
    ]