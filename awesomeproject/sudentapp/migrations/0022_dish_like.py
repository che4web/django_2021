# Generated by Django 3.2.7 on 2021-11-30 15:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sudentapp', '0021_auto_20211123_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
