# Generated by Django 4.2 on 2024-03-28 10:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0010_treatment_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='tid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
