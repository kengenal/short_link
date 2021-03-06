# Generated by Django 4.0.4 on 2022-05-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_link', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='link_id',
        ),
        migrations.RemoveField(
            model_name='links',
            name='main_url',
        ),
        migrations.AddField(
            model_name='links',
            name='new_url',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='links',
            name='url',
            field=models.URLField(default=None, unique=True),
        ),
    ]
