# Generated by Django 2.2.7 on 2019-12-02 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0003_auto_20191202_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_permissions',
        ),
    ]
