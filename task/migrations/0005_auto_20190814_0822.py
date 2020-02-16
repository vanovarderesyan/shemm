# Generated by Django 2.0.13 on 2019-08-14 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
        ('accountant', '0001_initial'),
        ('client', '0005_auto_20190813_0740'),
        ('task', '0004_auto_20190813_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('accountant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sms_accountant', to='accountant.Accountant')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sms_manager', to='client.Client')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sms_manager', to='manager.Manager')),
                ('task', models.ForeignKey(blank=True, default=None, on_delete='cascade', related_name='sms_task', to='task.Task')),
            ],
        ),
        migrations.RenameField(
            model_name='file',
            old_name='client',
            new_name='task',
        ),
    ]
