# Generated by Django 3.0.3 on 2020-07-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', unique=True),
        ),
    ]
