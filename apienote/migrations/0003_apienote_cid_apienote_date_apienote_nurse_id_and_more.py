# Generated by Django 4.1.13 on 2024-04-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apienote', '0002_alter_apienote_assessment_alter_apienote_evaluation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apienote',
            name='cid',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apienote',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apienote',
            name='nurse_id',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apienote',
            name='nurse_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
