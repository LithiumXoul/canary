# Generated by Django 3.0.8 on 2020-07-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nest', '0009_newsticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsticker',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
