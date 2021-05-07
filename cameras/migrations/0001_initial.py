# Generated by Django 3.2.2 on 2021-05-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('sensor', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Camera',
            },
        ),
    ]