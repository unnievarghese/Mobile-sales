# Generated by Django 3.1.6 on 2021-02-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile_model',
            name='mobile_image',
            field=models.ImageField(default='images', upload_to='images'),
            preserve_default=False,
        ),
    ]
