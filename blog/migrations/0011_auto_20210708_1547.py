# Generated by Django 3.1.3 on 2021-07-08 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210708_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='slug_field',
            new_name='slug',
        ),
    ]
