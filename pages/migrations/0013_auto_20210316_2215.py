# Generated by Django 3.1.6 on 2021-03-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_about_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='youtube_url',
            field=models.URLField(verbose_name='Hakkımızda Video Linki'),
        ),
    ]
