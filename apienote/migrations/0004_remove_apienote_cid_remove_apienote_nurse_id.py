# Generated by Django 4.1.13 on 2024-04-24 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apienote', '0003_apienote_cid_apienote_date_apienote_nurse_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apienote',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='apienote',
            name='nurse_id',
        ),
    ]
