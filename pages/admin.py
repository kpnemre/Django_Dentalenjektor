from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class GaleryTabularAdmin(admin.TabularInline):
    model = Galery
    
@admin.register(EkstraContent)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Icon)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Ekstra)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(EkstraType)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [GaleryTabularAdmin]
    list_display = ['title']


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_navbar', 'active', 'is_dropdown']
    list_filter = ['is_navbar', 'active', 'is_dropdown']
    list_editable = ['order', 'is_navbar', 'active', 'is_dropdown']

