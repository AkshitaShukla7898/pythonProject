# Generated by Django 2.1.5 on 2021-11-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0004_alter_data_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]