# Generated by Django 2.0.13 on 2019-08-13 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20190812_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='client',
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
    ]
