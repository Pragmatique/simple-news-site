# Generated by Django 2.2.7 on 2019-12-02 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 3, 0, 54, 56, 853783)),
        ),
    ]
