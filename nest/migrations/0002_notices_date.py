# Generated by Django 3.0.8 on 2020-07-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notices',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
