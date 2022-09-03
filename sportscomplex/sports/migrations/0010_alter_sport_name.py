# Generated by Django 4.0.6 on 2022-09-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0009_alter_sport_img_url_alter_sport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(help_text='Please, use underscore(_) or hypen(-) in place of spaces.', max_length=20, unique=True),
        ),
    ]
