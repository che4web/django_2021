# Generated by Django 3.2.7 on 2021-11-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0019_alter_dish_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='carbohydrate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Жиров на 100г'),
        ),
        migrations.AddField(
            model_name='food',
            name='energy',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='ккал на 100г'),
        ),
        migrations.AddField(
            model_name='food',
            name='fat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Жиров на 100г'),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Протеинов на 100г'),
        ),
    ]
