# Generated by Django 2.1.10 on 2019-07-16 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_review', '0003_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewer',
            name='response_token',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='view_token',
        ),
    ]