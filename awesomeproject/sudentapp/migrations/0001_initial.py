# Generated by Django 3.2.7 on 2021-10-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('recipe', models.TextField()),
                ('cooking_time', models.IntegerField()),
            ],
        ),
    ]
