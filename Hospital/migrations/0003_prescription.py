# Generated by Django 3.0.6 on 2020-05-24 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_usermore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescrip', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=100)),
                ('patient', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.UserDetails')),
            ],
        ),
    ]
