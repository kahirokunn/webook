# Generated by Django 2.0.1 on 2018-01-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webook', '0002_auto_20180124_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
