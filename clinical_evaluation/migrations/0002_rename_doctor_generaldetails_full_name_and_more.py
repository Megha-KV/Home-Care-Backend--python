# Generated by Django 4.1.13 on 2024-04-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical_evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generaldetails',
            old_name='doctor',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='generaldetails',
            old_name='h_f_name',
            new_name='ref_clinician',
        ),
        migrations.AlterField(
            model_name='generaldetails',
            name='op_no',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
