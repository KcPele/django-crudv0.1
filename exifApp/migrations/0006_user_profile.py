# Generated by Django 4.0.4 on 2022-07-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exifApp', '0005_rename_file_uploadimage_upload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('display_picture', models.FileField(upload_to='')),
            ],
        ),
    ]
