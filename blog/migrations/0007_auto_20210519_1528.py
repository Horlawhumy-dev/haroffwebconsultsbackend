# Generated by Django 3.1.3 on 2021-05-19 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210519_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='content1',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content3',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content4',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content5',
        ),
    ]
