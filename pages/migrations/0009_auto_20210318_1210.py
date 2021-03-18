# Generated by Django 3.1.6 on 2021-03-18 09:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_productcontent_producttitle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcontent',
            options={'verbose_name': 'Ürün Bilgi', 'verbose_name_plural': 'Ürün Bilgiler'},
        ),
        migrations.AlterModelOptions(
            name='producttitle',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.RenameField(
            model_name='productcontent',
            old_name='about',
            new_name='header',
        ),
        migrations.AddField(
            model_name='productcontent',
            name='image_def',
            field=models.CharField(blank=True, max_length=50, verbose_name='Ürün Resim Açıklaması'),
        ),
        migrations.AlterField(
            model_name='productcontent',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=250, verbose_name=' Ürün içerik'),
        ),
        migrations.AlterField(
            model_name='productcontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ürün Resim'),
        ),
        migrations.AlterField(
            model_name='productcontent',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Ürün Başlık'),
        ),
        migrations.AlterField(
            model_name='producttitle',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=250, verbose_name=' Ürünlerimiz içerik'),
        ),
        migrations.AlterField(
            model_name='producttitle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ürünlerimiz Sayfa Resim'),
        ),
        migrations.AlterField(
            model_name='producttitle',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Ürünlerimiz Başlık'),
        ),
    ]
