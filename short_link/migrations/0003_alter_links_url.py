# Generated by Django 4.0.4 on 2022-05-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_link', '0002_remove_links_link_id_remove_links_main_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]