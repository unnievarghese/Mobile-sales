# Generated by Django 3.1.6 on 2021-03-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0007_auto_20210312_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer_model',
            name='status',
            field=models.CharField(choices=[('New order', 'New order'), ('order confirmed', 'order confirmed'), ('dispatched', 'dispatched'), ('cancelled', 'cancelled')], default='New order', max_length=120, null=True),
        ),
    ]
