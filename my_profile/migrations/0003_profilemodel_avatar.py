# Generated by Django 4.1.1 on 2022-11-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_remove_profilemodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avatar',
            field=models.FileField(blank=True, upload_to='avatars'),
        ),
    ]
