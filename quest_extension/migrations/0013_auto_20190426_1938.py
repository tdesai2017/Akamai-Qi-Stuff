# Generated by Django 2.1.7 on 2019-04-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0012_auto_20190426_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='quest_path_number',
            field=models.IntegerField(),
        ),
    ]
