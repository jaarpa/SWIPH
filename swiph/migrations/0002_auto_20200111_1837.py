# Generated by Django 2.0.5 on 2020-01-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='Apr',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Aug',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Dec',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Feb',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Fri',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Jan',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Jul',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Jun',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Mar',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='May',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Mond',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Nov',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Oct',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Sat',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Sep',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Sun',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Thur',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Tues',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='Wend',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='demand',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='demandUnit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='hourEND',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='hourINI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='location',
            field=models.CharField(default='Daggett', max_length=200),
        ),
        migrations.AddField(
            model_name='simulation',
            name='pressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulation',
            name='tempIN',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
