# Generated by Django 5.1.2 on 2024-12-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_imageupload_remove_task_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
