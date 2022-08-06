# Generated by Django 4.0.6 on 2022-08-06 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exifApp', '0008_fileupload_delete_uploadimage_delete_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='created_at',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
