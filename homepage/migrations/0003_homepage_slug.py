# Generated by Django 4.2 on 2023-04-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_homepage_options_alter_homepage_code_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
