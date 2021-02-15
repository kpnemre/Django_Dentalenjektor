from django.contrib import admin
from .models import About
# Register your models here.



# admin.site.register(About)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=['title','sub_content','content','about_image','about_youtube_url']
    list_display_links=['title']
    search_fields=['title']
    list_filter=['title']
    # filtereleme yapar
    class Meta:
        model=About