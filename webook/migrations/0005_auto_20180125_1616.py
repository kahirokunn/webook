# Generated by Django 2.0.1 on 2018-01-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webook', '0004_auto_20180125_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='type',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')]),
        ),
    ]
