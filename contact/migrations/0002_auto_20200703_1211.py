# Generated by Django 2.2.7 on 2020-07-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(default=True, max_length=70),
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default=True, max_length=15),
        ),
    ]
