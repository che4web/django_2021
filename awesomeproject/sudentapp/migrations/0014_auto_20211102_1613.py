# Generated by Django 3.2.7 on 2021-11-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0013_dish_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['-name', 'cooking_time'], 'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AddField(
            model_name='dish',
            name='slug',
            field=models.CharField(default='test1', max_length=255, verbose_name='slug'),
            preserve_default=False,
        ),
    ]
