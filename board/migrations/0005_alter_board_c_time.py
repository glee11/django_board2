# Generated by Django 3.2.7 on 2021-10-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_c_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='c_time',
            field=models.DateTimeField(),
        ),
    ]
