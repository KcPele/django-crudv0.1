# Generated by Django 4.0.4 on 2022-07-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exifApp', '0002_rename_image_uploadimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]