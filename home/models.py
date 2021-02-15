from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class About(models.Model):
    title=models.CharField('Hakkımızda',max_length=200)
    sub_content = models.CharField("hakkımızda alt metin", max_length=250)
    content = RichTextField("içerik")
    about_image = models.ImageField("Hakkımızda kısmında çıkacak olan resim")
    about_youtube_url = models.URLField("Hakkımızda ile ilgili olan youtube URL'i ")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızdakiler'