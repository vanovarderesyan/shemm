# Generated by Django 2.0.13 on 2019-08-13 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190731_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='accountant',
            field=models.ManyToManyField(null=True, related_name='accountant_many_company', to='accountant.Accountant'),
        ),
        migrations.AlterField(
            model_name='company',
            name='client',
            field=models.ForeignKey(blank=True, default=None, on_delete='cascade', related_name='client_company', to='client.Client'),
        ),
        migrations.AlterField(
            model_name='company',
            name='subscribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribe', to='utils.Subscribe'),
        ),
    ]
