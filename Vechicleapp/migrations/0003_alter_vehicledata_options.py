# Generated by Django 4.1.2 on 2022-10-24 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vechicleapp', '0002_alter_vehicledata_vehicle_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicledata',
            options={'ordering': ('-date_added',)},
        ),
    ]
