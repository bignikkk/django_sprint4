# Generated by Django 3.2.16 on 2024-03-05 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240305_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_delayed',
        ),
        migrations.RemoveField(
            model_name='location',
            name='is_delayed',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_delayed',
        ),
    ]
