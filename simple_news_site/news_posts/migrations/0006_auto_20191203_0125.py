# Generated by Django 2.2.7 on 2019-12-02 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0005_auto_20191203_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 3, 1, 25, 14, 585783)),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug-field', max_length=250),
        ),
    ]
