# Generated by Django 4.2 on 2023-04-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0005_coding_slug_argomento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coding',
            name='argomento',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
