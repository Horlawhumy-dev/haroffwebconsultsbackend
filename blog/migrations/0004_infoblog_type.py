# Generated by Django 3.1.3 on 2021-05-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210322_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoblog',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
