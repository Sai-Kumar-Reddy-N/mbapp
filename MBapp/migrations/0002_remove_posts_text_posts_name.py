# Generated by Django 4.0.4 on 2022-04-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='text',
        ),
        migrations.AddField(
            model_name='posts',
            name='Name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
