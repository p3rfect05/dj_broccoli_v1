# Generated by Django 4.1.1 on 2022-11-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_gallerystoragemodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerystoragemodel',
            name='image',
            field=models.FileField(upload_to='../gallery'),
        ),
    ]