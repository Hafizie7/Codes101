# Generated by Django 3.0 on 2019-12-18 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20191218_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='CustomerID',
            new_name='RoomNo',
        ),
    ]
