# Generated by Django 2.1.7 on 2019-05-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0011_project_project_admin_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_admin_pin',
            field=models.CharField(default='0', max_length=255, unique=True),
        ),
    ]