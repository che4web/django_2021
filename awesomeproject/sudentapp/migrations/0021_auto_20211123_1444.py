# Generated by Django 3.2.7 on 2021-11-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0020_auto_20211123_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbohydrate',
            field=models.FloatField(default=0, verbose_name='Жиров на 100г'),
        ),
        migrations.AlterField(
            model_name='food',
            name='energy',
            field=models.FloatField(default=0, verbose_name='ккал на 100г'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(default=0, verbose_name='Жиров на 100г'),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(default=0, verbose_name='Протеинов на 100г'),
        ),
    ]
