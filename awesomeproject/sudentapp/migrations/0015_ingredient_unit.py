# Generated by Django 3.2.7 on 2021-11-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudentapp', '0014_auto_20211102_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('KG', 'килиграмм'), ('G', 'грамм'), ('U', 'штук')], default='U', max_length=2),
            preserve_default=False,
        ),
    ]