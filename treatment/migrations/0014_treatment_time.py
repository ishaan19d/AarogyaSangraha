# Generated by Django 4.2 on 2024-03-28 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0013_treatment_suggestions_alter_treatment_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
