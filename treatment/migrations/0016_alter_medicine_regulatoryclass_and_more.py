# Generated by Django 4.2 on 2024-03-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0015_medicine_dosage_alter_treatment_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='regulatoryClass',
            field=models.CharField(choices=[('General', 'General'), ('Restricted', 'Restricted')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='type_med',
            field=models.CharField(choices=[('Antipyretic', 'Antipyretic'), ('Analgesic', 'Analgesic'), ('Antihistamine', 'Antihistamine'), ('Antibiotic', 'Antibiotic'), ('Antidepressant', 'Antidepressant'), ('Anticoagulant', 'Anticoagulant'), ('Antihypertensive', 'Antihypertensive'), ('Anti-inflammatory', 'Anti-inflammatory'), ('Antiviral', 'Antiviral'), ('Diuretic', 'Diuretic')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
