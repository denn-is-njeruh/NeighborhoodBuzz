# Generated by Django 3.2.7 on 2021-09-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
