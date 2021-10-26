# Generated by Django 3.2.7 on 2021-10-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0002_auto_20211026_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('quantity', models.FloatField(verbose_name=' колличество ')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sudentapp.dish')),
            ],
        ),
    ]
