# Generated by Django 4.2.5 on 2023-10-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingc', '0002_alter_appointmentc_service_alter_appointmentc_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentc',
            name='service',
            field=models.CharField(choices=[('Urinary tract infection for women', 'Urinary tract infection for women'), ('Contraception', 'Contraception'), ('Skin conditions', 'Skin conditions'), ('Ear conditions', 'Ear conditions'), ('Sore throat test & treat', 'Sore throat test & treat'), ('Flu Vaccination', 'Flu Vaccination')], default='Doctor care', max_length=50),
        ),
    ]