# Generated by Django 4.2 on 2024-03-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0007_hospitalregistrationrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending Verification'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
