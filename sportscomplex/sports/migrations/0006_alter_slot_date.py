# Generated by Django 4.0.6 on 2022-09-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0005_alter_booking_booked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.DateField(),
        ),
    ]
