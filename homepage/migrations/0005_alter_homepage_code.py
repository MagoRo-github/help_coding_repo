# Generated by Django 4.2 on 2023-04-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_homepage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
