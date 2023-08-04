# Generated by Django 4.2.3 on 2023-07-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0003_donation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation_table',
            name='donation_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]