# Generated by Django 2.1.7 on 2019-05-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0025_auto_20190531_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MC', 'MC'), ('FR', 'FR'), ('API', 'API')], max_length=45),
        ),
    ]