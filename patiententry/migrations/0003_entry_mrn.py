# Generated by Django 4.1.13 on 2024-05-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patiententry', '0002_remove_entry_nurse_id_remove_entry_updated_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='mrn',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
