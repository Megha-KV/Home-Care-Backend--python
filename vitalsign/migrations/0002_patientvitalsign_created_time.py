# Generated by Django 4.1.13 on 2024-04-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitalsign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvitalsign',
            name='created_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
