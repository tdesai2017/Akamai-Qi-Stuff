# Generated by Django 2.1.7 on 2019-04-26 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0009_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest_extension.Project'),
        ),
    ]
