# Generated by Django 3.1.3 on 2021-03-22 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_showcaseblog_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showcaseblog',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
