# Generated by Django 3.1.6 on 2021-03-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_homefooterup_rightcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homefooterup',
            name='rightcontent',
            field=models.CharField(blank=True, max_length=75, verbose_name='Sağiçerik'),
        ),
    ]
