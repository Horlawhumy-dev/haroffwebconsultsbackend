# Generated by Django 3.1.3 on 2021-03-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210317_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoblog',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
