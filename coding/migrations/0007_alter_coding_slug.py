# Generated by Django 4.2 on 2023-05-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0006_alter_coding_argomento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coding',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
