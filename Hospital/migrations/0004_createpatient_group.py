# Generated by Django 3.0.6 on 2020-05-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_auto_20200525_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpatient',
            name='group',
            field=models.CharField(max_length=50, null=True),
        ),
    ]