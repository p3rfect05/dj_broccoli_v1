# Generated by Django 4.1.6 on 2023-02-21 19:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0011_alter_profilemodel_date'),
        ('main_menu', '0006_sessiontoken_user_sessiontoken_vk_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpmodel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_author', to='my_profile.profilemodel'),
        ),
        migrations.AlterField(
            model_name='helpmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]