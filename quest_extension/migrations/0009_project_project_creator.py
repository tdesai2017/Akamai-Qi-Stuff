# Generated by Django 2.1.7 on 2019-05-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0008_auto_20190516_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quest_extension.Admin'),
        ),
    ]
