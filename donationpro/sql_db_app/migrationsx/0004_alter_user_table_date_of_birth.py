# Generated by Django 4.2.3 on 2023-07-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_db_app', '0003_alter_user_table_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
             name='date_of_birth',
             field=models.DateField(),
        ),
    ]