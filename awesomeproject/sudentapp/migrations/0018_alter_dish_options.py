# Generated by Django 3.2.7 on 2021-11-18 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0017_alter_dish_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['-name', 'cooking_time'], 'permissions': [('my_permission', 'Это мое особое разрешение')], 'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
    ]