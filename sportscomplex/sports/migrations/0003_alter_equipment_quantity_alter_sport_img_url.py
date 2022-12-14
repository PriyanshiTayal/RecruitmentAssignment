# Generated by Django 4.0.6 on 2022-08-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='quantity',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='img_url',
            field=models.CharField(default='https://uploads-ssl.webflow.com/617b224ba2374548fcc039ba/617b224ba237453ce1c0409b_hpfulq-1234-1024x512.jpg', max_length=2083),
        ),
    ]
