# Generated by Django 4.2 on 2024-03-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0016_alter_medicine_regulatoryclass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='medicines',
            field=models.ManyToManyField(through='treatment.Medicine_Treatment', to='treatment.medicine'),
        ),
    ]
