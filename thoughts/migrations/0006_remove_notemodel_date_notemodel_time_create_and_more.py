# Generated by Django 4.1.6 on 2023-02-18 21:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0008_alter_profilemodel_last_name'),
        ('thoughts', '0005_alter_notemodel_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notemodel',
            name='date',
        ),
        migrations.AddField(
            model_name='notemodel',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notemodel',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='my_profile.profilemodel'),
        ),
    ]
