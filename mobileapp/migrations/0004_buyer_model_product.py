# Generated by Django 3.1.6 on 2021-03-11 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0003_buyer_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer_model',
            name='product',
            field=models.CharField(max_length=120, null=True),
        ),
    ]