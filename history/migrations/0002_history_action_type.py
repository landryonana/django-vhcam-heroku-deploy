# Generated by Django 2.2.24 on 2021-08-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='action_type',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
