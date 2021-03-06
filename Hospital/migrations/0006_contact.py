# Generated by Django 3.0.6 on 2020-05-25 10:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_patientinvoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None)),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
    ]
