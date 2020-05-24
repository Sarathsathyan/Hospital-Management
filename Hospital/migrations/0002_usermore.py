# Generated by Django 3.0.6 on 2020-05-24 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('case', models.IntegerField()),
                ('blood', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.UserDetails')),
            ],
        ),
    ]