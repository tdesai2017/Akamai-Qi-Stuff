# Generated by Django 2.1.7 on 2019-05-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0016_auto_20190520_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='undo_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
