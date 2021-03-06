# Generated by Django 2.0.13 on 2019-07-31 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CardService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('text', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('text', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('text', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('text', models.CharField(blank=True, max_length=255)),
                ('to', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='packages',
            name='service',
            field=models.ManyToManyField(related_name='service_many', to='utils.Service', verbose_name='service_many'),
        ),
    ]
