# Generated by Django 4.1.6 on 2023-06-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_eventmodel_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
