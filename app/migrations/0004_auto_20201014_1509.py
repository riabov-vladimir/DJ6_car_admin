# Generated by Django 2.2.13 on 2020-10-14 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201014_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
    ]
