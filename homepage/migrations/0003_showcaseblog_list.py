# Generated by Django 3.1.3 on 2021-03-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_showcaseblog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcaseblog',
            name='list',
            field=models.BooleanField(null=True),
        ),
    ]
