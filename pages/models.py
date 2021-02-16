from django.db import models
from django.utils.text import slugify


class Header(models.Model):
    title = models.CharField("Başlık", max_length = 75)
    slug = models.SlugField("site", editable = False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    content = models.TextField("İçeirk", blank = True)
    description = models.CharField("Sayfanın search engine açıklaması", max_length = 120)
    is_navbar = models.BooleanField("Navbarda gösterilsin mi?", default = True)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    order = models.SmallIntegerField("Sıralama", default = 0)
    
    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField("Başlık", max_length = 75, unique = True)
    slug = models.SlugField("site", editable = False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    header = models.ForeignKey("pages.Header", related_name="pages", blank = True, null = True, on_delete = models.CASCADE)
    description = models.CharField("Sayfanın search engine açıklaması", max_length = 120)
    keywords  = models.CharField("Sayfanın search engine anahtar kelimeleri", max_length = 120)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    order = models.SmallIntegerField("Sıralama", default = 0)

    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace("ı", "i").replace("I", "i").lower())
        super(Page, self).save(*args, **kwargs)
        


class Galery(models.Model):
    image = models.ImageField("resim")
    short_description = models.CharField("Kısa açıklama", max_length=75)
    content = models.TextField("Açıklama")
    page = models.ForeignKey("pages.Page", on_delete = models.CASCADE, null = True, blank = True)
    
    def __str__(self):
      return self.short_description  
        