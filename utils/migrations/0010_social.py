# Generated by Django 2.0.13 on 2019-09-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0009_staff_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.TextField(blank=True, max_length=255)),
                ('image', models.FileField(blank=True, max_length=255, upload_to='')),
            ],
        ),
    ]
