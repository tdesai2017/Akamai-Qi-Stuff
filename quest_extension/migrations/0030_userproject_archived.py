# Generated by Django 2.1.7 on 2019-06-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0029_adminproject_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
