# Generated by Django 3.2.5 on 2021-08-26 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_app', '0005_rename_order_id_buyer_buyer_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='buyer_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='buyer_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
