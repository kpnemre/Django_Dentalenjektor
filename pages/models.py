from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Home(models.Model):
    title = models.CharField("Başlık", max_length = 75)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    herocontent= models.CharField("Slayt içindeki yazı", max_length=150)
    subherocontent=models.CharField("Slayt içindeki alt yazı", blank=True, max_length=150)
    image = models.ImageField("resim", null = True, blank = True)
    pagemaintitle= models.CharField("Ana sayfa ana başlığı", max_length=150)
    pagesubcontent=models.CharField("Ana sayfa alt içerik", blank=True, max_length=150)
    below_title=models.CharField("Alt Başlık", blank=True, max_length=150)
    below_image = models.ImageField("Alt Resim", null = True, blank = True)
    below_content=models.CharField("Alt içerik", blank=True, max_length=200)
    last_title=models.CharField("En Alt Başlık", blank=True, max_length=75)
    last_image1= models.ImageField("En Alt Resim", null = True, blank = True)
    last_image2= models.ImageField("En Alt Resim", null = True, blank = True)
    last_content=models.CharField("En Alt içerik", blank=True, max_length=200) 
      
    description = models.CharField("Sayfanın search engine açıklaması", max_length = 120)
    is_navbar = models.BooleanField("Navbarda gösterilsin mi?", default = True)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    order = models.SmallIntegerField("Sıralama", default = 0)
    is_dropdown = models.BooleanField("Alt başlıkları olsun mu", default = False)
    # template = models.ForeignKey("pages.Template", on_delete = models.SET_NULL, null = True, blank = True)
    # ekstras = models.ManyToManyField("pages.Ekstra", null = True, blank = True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "AnaSayfa Ana İçerik "
        verbose_name ="AnaSayfa Ana İçerikler "
    
    
    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title.replace("ı", "i").replace("I", "i").lower())
    #     super(Header, self).save(*args, **kwargs)

class HomeDetail(models.Model):
    title = models.CharField("Başlık", max_length = 75)
    content = RichTextField("İçerik")
    image = models.ImageField("resim", null = True, blank = True)
    order = models.SmallIntegerField("Sıralama", default = 0)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Anasayfa Şerit İçerikler"
        verbose_name ="Anasayfa Şerit İçerik"
        
    def __str__(self): 
        return self.title

class HomeMiddleHeader(models.Model):
    title=models.CharField(" Başlık", blank=True, max_length=150)
    image = models.ImageField(" Resim", null = True, blank = True)
    content=models.CharField(" Başlık içerik", blank=True, max_length=250)
    order = models.SmallIntegerField("Sıralama", default = 0)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Ana Sayfa ikinci  Alan İçerikler"
        verbose_name ="Ana Sayfa ikinci Alan İçerik"
        
    def __str__(self): 
        return self.title
    
class HomeMiddleDetail(models.Model):
    header = models.ForeignKey(HomeMiddleHeader, null= True, blank = True, on_delete = models.CASCADE)
    title = models.CharField("Başlık", max_length = 75)
    content = RichTextField("İçerik")
    order = models.SmallIntegerField("Sıralama", default = 0)
    # icon = models.ForeignKey("pages.Icon", null= True, blank = True, on_delete = models.CASCADE)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Ana Sayfa Orta Alan Detaylar"
        verbose_name ="Ana Sayfa Orta Alan Detay" 
        
    def __str__(self): 
        return self.title
        
# class HomeIcon(models.Model):
#     title = models.CharField("Başlık", max_length = 75)
#     order = models.SmallIntegerField("Sıralama", default = 0)
#     icon = models.ForeignKey("pages.Icon", null= True, blank = True, on_delete = models.CASCADE)
#     active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    
    
#     class Meta:
#         ordering = ['order']
#         verbose_name_plural = "Anasayfa Alt İconlar"
#         verbose_name ="Anasayfa Alt İcon" 
        
#     def __str__(self): 
#         return self.title
   
class HomeFooterUp(models.Model):
    title = models.CharField("Başlık", max_length = 75)
    order = models.SmallIntegerField("Sıralama", default = 0)
    active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    content1 = models.CharField("İçerik1", max_length = 75, blank=True)
    content2 = models.CharField("İçerik2", max_length = 75, blank=True)
    content3 = models.CharField("İçerik3", max_length = 75, blank=True)
    content4 = models.CharField("İçerik4", max_length = 75, blank=True)
    content5 = models.CharField("İçerik5", max_length = 75, blank=True)
    content6 = models.CharField("İçerik6", max_length = 75, blank=True)
    rightcontent=models.CharField("Sağiçerik", max_length = 75, blank=True)
    
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Anasayfa Footer Üstü Kartlar"
        verbose_name ="Anasayfa Footer Üstü Kart"  
        
    def __str__(self): 
        return self.title    

# class Icon (models.Model):
#     title = models.CharField("İcon adı", max_length = 75)
    
#     def __str__(self):
#         return self.title        
        
             
class ContactInfo(models.Model):
    name = models.CharField("İSİM:", max_length = 30)
    email = models.EmailField("Eposta adresi:")
    # number = models.SmallIntegerField("Telefon Numaranız:")
    message = models.TextField("Mesajınız:")
    # active = models.BooleanField("Sitede gösterilsin mi?", default = True)
    # publish_date=models.DateTimeField("Yayınlanma Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = 'Gelen Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'

    def __str__(self):
        return self.name   

class About(models.Model):
    about_title= models.CharField("Hakkımızda Resim Ortası Başlık", max_length=50)
    about_main_image= models.ImageField("Hakkımızda Ana Resim", null = True, blank = True)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da çıkması için gerekli anahtar kelimeler", max_length=150)
    images_title= models.CharField("Hakkımızda Resimler Başlık", max_length=50)
    images_content= models.TextField("Hakkımızda Resimler İçerik", max_length=50)
    youtube_url = models.URLField("Hakkımızda Video Linki")
    button_name= models.CharField("Hakkımızda Video Buton Üzerindeki Yazı", max_length=50)
    images_image1= models.ImageField("Hakkımızda Resimler Resim1", null = True, blank = True)
    images_image1_content= models.CharField("Hakkımızda Resimler Resim1 açıklaması", max_length=50)
    images_image2= models.ImageField("Hakkımızda Resimler Resim2", null = True, blank = True)
    images_image2_content= models.CharField("Hakkımızda Resimler Resim2 açıklaması", max_length=50)
    images_image3= models.ImageField("Hakkımızda Resimler Resim3", null = True, blank = True)
    images_image3_content= models.CharField("Hakkımızda Resimler Resim3 açıklaması", max_length=50)
    images_image4= models.ImageField("Hakkımızda Resimler Resim4", null = True, blank = True)
    images_image4_content= models.CharField("Hakkımızda Resimler Resim4 açıklaması", max_length=50)
    middle_title=models.CharField("Hakkımızda Footer Üstü Başlık", blank = True, max_length=50)
    middle_content=models.CharField("Hakkımızda Footer Üstü İçerik", blank = True, max_length=100)
    middle_image1= models.ImageField("Hakkımızda Footer Üstü Resim",blank = True)
    middle_image1_content= models.CharField("Hakkımızda Footer Üstü Resim Açıklaması",blank = True, max_length=50)
    middle_image2= models.ImageField("Hakkımızda Footer Üstü Resim", blank = True)
    middle_image2_content= models.CharField("Hakkımızda Footer Üstü Resim Açıklaması", blank = True, max_length=50)
    
    
    
    class Meta:
        verbose_name = 'Hakkımızda İçerik'
        verbose_name_plural = 'Hakkımızda İçerikler'

    def __str__(self):
        return self.about_title 
    
    
class AboutContent(models.Model):
    about = models.ForeignKey(About, on_delete = models.CASCADE, related_name='aboutcontent')
    title= models.CharField("Hakkımızda Başlık", max_length=50)
    image= models.ImageField("Hakkımızda Resim", null = True, blank = True)
    content=RichTextField(" Hakkımızda içerik", blank=True, max_length=250)
    
    class Meta:
        verbose_name = 'Hakkımızda Bilgi'
        verbose_name_plural = 'Hakkımızda Bilgiler'

    def __str__(self):
        return self.title 
    
class Services(models.Model):
    title= models.CharField("Ana Başlık", max_length=50)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    main_image= models.ImageField("Ana Resim", null = True, blank = True)
    card1_title= models.CharField("Hizmetler Başlık", max_length=50)
    card1_content= RichTextField("Hizmetler Açıklama")
    card1_image= models.ImageField("Hizmetler Resim", null = True, blank = True)
    card1_image_cont= models.CharField("Hizmetler Resim Açıklaması", max_length=50)
    card2_title= models.CharField("Hizmetler Başlık", max_length=50)
    card2_content= RichTextField("Hizmetler Açıklama")
    card2_image= models.ImageField("Hizmetler Resim", null = True, blank = True)
    card2_image_cont= models.CharField("Hizmetler Resim Açıklaması", max_length=50)
    
    
    class Meta:
        verbose_name = 'Hizmetler İçerik'
        verbose_name_plural = 'Hizmetler İçerikler'

    def __str__(self):
        return self.title 

class ProductTitle(models.Model):
    title= models.CharField("Ürünlerimiz Resim üzeri Başlık", max_length=50)
    product_title= models.CharField("Ürünlerimiz Başlık",blank = True, max_length=50)
    image= models.ImageField("Ürünlerimiz Sayfa Resim", null = True, blank = True)
    content=RichTextField(" Ürünlerimiz içerik", blank=True)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    
    
    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.title


class ProductContent(models.Model):
    header = models.ForeignKey(ProductTitle, on_delete = models.CASCADE, related_name='aboutcontent')
    title= models.CharField("Ürün Başlık", max_length=50)
    image= models.ImageField("Ürün Resim", null = True, blank = True)
    image_def= models.CharField("Ürün Resim Açıklaması", blank = True, max_length=50)
    content=RichTextField(" Ürün içerik", blank=True)
    
    class Meta:
        verbose_name = 'Ürün Bilgi'
        verbose_name_plural = 'Ürün Bilgiler'

    def __str__(self):
        return self.title  
    
    
      
# class Products(models.Model):
#     title = models.CharField("Ürünler Başlık", max_length=50)
#     content= RichTextField("Ürünler Açıklama")

#     class Meta:
#         verbose_name = 'Ürün'
#         verbose_name_plural = 'Ürünler '

#     def __str__(self):
#         return self.title 

# class Productsdetail(models.Model):
#     header = models.ForeignKey(Products, on_delete = models.CASCADE, related_name='products')
#     title = models.CharField("Ürün Başlığı", max_length=50)
#     content= RichTextField("Ürün Bilgisi")

#     class Meta:
#         verbose_name = 'Ürünler İçerik'
#         verbose_name_plural = 'Ürünler İçerikler'

#     def __str__(self):
#         return self.title 

     
class Setting(models.Model):
    title = models.CharField("title", max_length=50)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    description_contact = models.CharField("İletişim Sayfası için Google'da çıkacak olan yazı", max_length=150)
    keywords_contact = models.CharField(" İletişim Sayfası için Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    copyright_name = models.CharField(max_length=50, default="KaanFilo")
    adress = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    whatsapp_phone = models.CharField(max_length=20,default="")
    navmessage = models.CharField("Site en üstünde verilecek mesaj", blank=True, max_length = 75)
    logo1 = models.ImageField("logo1", upload_to='setting/',default = "Rasyonel Dental")
    logo2 = models.ImageField("logo2", upload_to='setting/',default = "Rasyonel Dental")
    contact_page_image =  models.ImageField("İletişim Sayfası Ana Resim", null = True, blank = True)
    # image = models.ImageField("Hakkımızda kısmı için resim", blank=True, null=True)
    # content = models.TextField("Hakkımızda kısmı için içerik:")
    favicon = models.ImageField("Favicon resim", blank=True, null=True)
    googleMap= models.CharField("Googlemap iframe", blank=True, null=True, max_length=200)
    contactmessage= models.CharField("İletişim mesajı", blank=True, max_length=150)
    # contact_image = models.ImageField("Hakkımızda kısmı için resim", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'
    def __str__(self):
        return self.title
        
        
             

# class Template(models.Model):
#     name = models.CharField("html template", max_length=50)
#     #ekstras = models.ManyToManyField('pages.EkstraContent', null = True, blank = True)
    
#     def __str__(self):
#         return self.name

# class Ekstra(models.Model):
#     title = models.CharField("Başlık", max_length=50)
#     #ekstra_contents = models.ManyToManyField('pages.EkstraContent', null = True, blank = True)
#     #html_code = models.TextField("Html kodu")
#     ekstra_tipi = models.ForeignKey("pages.EkstraType", null = True, blank = True, on_delete = models.SET_NULL)
    
#     def __str__(self):
#         return self.title


# class EkstraType(models.Model):
#     title = models.CharField("Başlık", max_length=50)
    
#     def __str__(self):
#         return self.title


# class EkstraContent(models.Model):
#     title = models.CharField("başlık", max_length=50)
#     short_content = models.CharField("kısa açıklama", max_length=75)
#     image = models.ImageField("resim", null = True, blank = True)
#     icon = models.ForeignKey("pages.Icon", null = True, blank = True, on_delete=models.SET_NULL)
#     ekstra = models.ForeignKey("pages.Ekstra", null = True, blank = True, on_delete=models.SET_NULL)
#     def __str__(self):
#         return self.title
    
    
    
# class Page(models.Model):
#     title = models.CharField("Başlık", max_length = 75, unique = True)
#     slug = models.SlugField("site", editable = False)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
#     header = models.ForeignKey("pages.Header", related_name="pages", blank = True, null = True, on_delete = models.CASCADE)
#     description = models.CharField("Sayfanın search engine açıklaması", max_length = 120)
#     keywords  = models.CharField("Sayfanın search engine anahtar kelimeleri", max_length = 120)
#     active = models.BooleanField("Sitede gösterilsin mi?", default = True)
#     order = models.SmallIntegerField("Sıralama", default = 0)
#     short_content = models.CharField("Kısa Açıklama", max_length=75)
#     content = RichTextField("Açıklama")
#     icon = models.ForeignKey("pages.Icon", null= True, blank = True, on_delete = models.SET_NULL)
    
#     def __str__(self):
#         return self.title
    
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title.replace("ı", "i").replace("I", "i").lower())
#         super(Page, self).save(*args, **kwargs)
        


    
    
    
# class Galery(models.Model):
#     image = models.ImageField("resim")
#     short_description = models.CharField("Kısa açıklama", max_length=75)
#     content = models.TextField("Açıklama")
#     page = models.ForeignKey("pages.Page", on_delete = models.CASCADE, null = True, blank = True)
    
#     def __str__(self):
#       return self.short_description  
        