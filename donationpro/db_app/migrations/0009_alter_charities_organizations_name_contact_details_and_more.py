# Generated by Django 4.2.3 on 2023-08-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0008_charities_organizations_name_contact_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charities_organizations_name',
            name='contact_details',
            field=models.CharField(default='contact number', max_length=25),
        ),
        migrations.AlterField(
            model_name='charities_organizations_name',
            name='description',
            field=models.CharField(default='decription of organization', max_length=500),
        ),
        migrations.AlterField(
            model_name='charities_organizations_name',
            name='email',
            field=models.CharField(default='example@example.com', max_length=200),
        ),
    ]
