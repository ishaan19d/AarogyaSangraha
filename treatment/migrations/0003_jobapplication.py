# Generated by Django 4.2 on 2024-03-26 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0002_rename_date_birth_patient_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(auto_now_add=True)),
                ('experience', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.hospital')),
                ('medical_practitioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.medicalpractitioner')),
            ],
        ),
    ]
