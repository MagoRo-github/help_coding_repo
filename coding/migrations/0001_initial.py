# Generated by Django 4.2 on 2023-04-25 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0002_alter_homepage_options_alter_homepage_code_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linguaggio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.homepage')),
            ],
        ),
    ]
