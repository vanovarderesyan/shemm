# Generated by Django 2.0.13 on 2019-08-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20190814_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
