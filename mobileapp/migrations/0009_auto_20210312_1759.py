# Generated by Django 3.1.6 on 2021-03-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0008_buyer_model_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_model',
            name='status',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
