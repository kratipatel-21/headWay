# Generated by Django 3.2.6 on 2021-08-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wayahead', '0003_rename_deflevel_question_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='status',
        ),
        migrations.AddField(
            model_name='question',
            name='point',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
