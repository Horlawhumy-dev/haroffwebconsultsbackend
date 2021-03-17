# Generated by Django 3.1.3 on 2021-03-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210317_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog_title',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='commentator_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
