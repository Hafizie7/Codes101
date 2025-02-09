# Generated by Django 3.0 on 2019-12-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20191218_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('CustomerName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='double_bed',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Room is available'), ('RESERVED', 'Room already reserved')], default='Available', max_length=10),
        ),
        migrations.AlterField(
            model_name='singlebed',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Room is available'), ('RESERVED', 'Room already reserved')], default='Available', max_length=10),
        ),
    ]
