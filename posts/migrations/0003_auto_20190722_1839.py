# Generated by Django 2.2.2 on 2019-07-22 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
    ]
