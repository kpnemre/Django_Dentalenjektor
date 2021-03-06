# Generated by Django 3.1.6 on 2021-03-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210321_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='keywords',
            field=models.CharField(default=1, max_length=150, verbose_name="Google'da çıkması için gerekli anahtar kelimeler"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttitle',
            name='keywords',
            field=models.CharField(default=1, max_length=150, verbose_name="Google'da aramalarda çıkabilmek için gerekli anahtar kelimler"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='keywords',
            field=models.CharField(default=1, max_length=150, verbose_name="Google'da aramalarda çıkabilmek için gerekli anahtar kelimler"),
            preserve_default=False,
        ),
    ]
