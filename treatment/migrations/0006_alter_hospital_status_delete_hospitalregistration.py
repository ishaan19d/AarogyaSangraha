# Generated by Django 4.2 on 2024-03-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0005_hospitalregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='HospitalRegistration',
        ),
    ]
