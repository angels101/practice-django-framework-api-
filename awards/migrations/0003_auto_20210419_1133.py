# Generated by Django 3.2 on 2021-04-19 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20210417_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='following',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
