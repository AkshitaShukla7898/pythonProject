# Generated by Django 3.2.5 on 2021-09-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0003_data_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='gender',
            field=models.IntegerField(choices=[('', 'Select'), (0, 'girl'), (1, 'boy')]),
        ),
    ]
