# Generated by Django 3.2.7 on 2021-10-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0005_dish_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Food',
            new_name='Ingredient',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='date',
        ),
    ]
