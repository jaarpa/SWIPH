# Generated by Django 2.0.5 on 2020-01-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiph', '0005_auto_20200112_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='nModBoil',
            field=models.IntegerField(default=4),
        ),
    ]
