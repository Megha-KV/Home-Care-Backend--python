# Generated by Django 4.1.13 on 2024-04-28 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitalsign', '0004_patientvitalsign_infant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvitalsign',
            old_name='mrn',
            new_name='mr_no',
        ),
    ]
