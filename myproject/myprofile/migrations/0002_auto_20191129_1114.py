# Generated by Django 2.2.7 on 2019-11-29 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='introduce',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='published_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
