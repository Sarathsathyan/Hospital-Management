# Generated by Django 3.0.6 on 2020-05-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_auto_20200525_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpatient',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='createpatient',
            name='case',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='createpatient',
            name='out',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='createpatient',
            name='paid',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
