from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Header(models.Model):
    title = models.CharField("Başlık", max_length = 75)
    slug = models.SlugField("site", editable = False, default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    content = RichTextField("İçeirk")
    description = models.CharField("Sayfanın search engine açıklaması", max_length = 120)
    is_navbar = models.BooleanField("Navbarda gösterilsin mi?", default = True)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    order = models.SmallIntegerField("Sıralama", default = 0)
    is_dropdown = models.BooleanField("Alt başlıkları olsun mu", default = False)
    template = models.ForeignKey("pages.Template", on_delete = models.SET_NULL, null = True, blank = True)
    ekstras = models.ManyToManyField("pages.Ekstra", null = True, blank = True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Başlıklar"
        verbose_name ="Başlık"
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace("ı", "i").replace("I", "i").lower())
        super(Header, self).save(*args, **kwargs)
        

class Template(models.Model):
    name = models.CharField("html template", max_length=50)
    #ekstras = models.ManyToManyField('pages.EkstraContent', null = True, blank = True)
    
    def __str__(self):
        return self.name

class Ekstra(models.Model):
    title = models.CharField("Başlık", max_length=50)
    #ekstra_contents = models.ManyToManyField('pages.EkstraContent', null = True, blank = True)
    #html_code = models.TextField("Html kodu")
    ekstra_tipi = models.ForeignKey("pages.EkstraType", null = True, blank = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.title


class EkstraType(models.Model):
    title = models.CharField("Başlık", max_length=50)
    
    def __str__(self):
        return self.title


class EkstraContent(models.Model):
    title = models.CharField("başlık", max_length=50)
    short_content = models.CharField("kısa açıklama", max_length=75)
    image = models.ImageField("resim", null = True, blank = True)
    icon = models.ForeignKey("pages.Icon", null = True, blank = True, on_delete=models.SET_NULL)
    ekstra = models.ForeignKey("pages.Ekstra", null = True, blank = True, on_delete=models.SET_NULL)
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
    short_content = models.CharField("Kısa Açıklama", max_length=75)
    content = RichTextField("Açıklama")
    icon = models.ForeignKey("pages.Icon", null= True, blank = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace("ı", "i").replace("I", "i").lower())
        super(Page, self).save(*args, **kwargs)
        

class Icon (models.Model):
    title = models.CharField("İcon adı", max_length = 75)
    
    def __str__(self):
        return self.title
    
    
    
class Galery(models.Model):
    image = models.ImageField("resim")
    short_description = models.CharField("Kısa açıklama", max_length=75)
    content = models.TextField("Açıklama")
    page = models.ForeignKey("pages.Page", on_delete = models.CASCADE, null = True, blank = True)
    
    def __str__(self):
      return self.short_description  
        