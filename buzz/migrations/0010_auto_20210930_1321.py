# Generated by Django 3.2.7 on 2021-09-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzz', '0009_profile_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
