# Generated by Django 2.1.7 on 2019-04-24 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_extension', '0007_auto_20190423_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incorrectanswer',
            old_name='incorrect_answer_text',
            new_name='answer_text',
        ),
    ]
