# Generated by Django 4.0.6 on 2022-09-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0012_alter_slot_end_time_alter_slot_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.DateField(help_text='(Date should be of format YYYY-MM-DD)'),
        ),
    ]
