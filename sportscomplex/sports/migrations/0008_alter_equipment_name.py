# Generated by Django 4.0.6 on 2022-09-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0007_alter_equipment_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
