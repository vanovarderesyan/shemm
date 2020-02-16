# Generated by Django 2.0.13 on 2019-08-12 10:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0007_auto_20190806_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('image', models.FileField(blank=True, max_length=255, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='main',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
    ]
