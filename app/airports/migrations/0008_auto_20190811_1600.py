# Generated by Django 2.2.4 on 2019-08-11 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0007_auto_20190811_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequency',
            name='type',
            field=models.CharField(max_length=16),
        ),
    ]