# Generated by Django 2.2.2 on 2019-06-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('custom_id', models.IntegerField()),
                ('category', models.CharField(choices=[('Dj', 'Django'), ('R', 'Ruby')], max_length=3)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
