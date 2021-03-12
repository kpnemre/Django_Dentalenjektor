from django.contrib import admin
from django.utils.translation import gettext_lazy as _
import nested_admin
from .models import *


class EkstraContentInline(nested_admin.NestedTabularInline):  # ınline olarak hazırlıyor
    model = EkstraContent
    extra = 4
    max_num = 8
    
class EkstraInline(nested_admin.NestedTabularInline):
    model = Ekstra
    inlines = [EkstraContentInline]
    extra = 1
    max_num = 10

class EkstraTypeAdmin(nested_admin.NestedModelAdmin):
    model = EkstraType
    inlines = [EkstraInline]

class GaleryTabularAdmin(admin.TabularInline):
    model = Galery
    
# class ExtraTabularInline(admin.TabularInline):
#     model = Ekstra


# @admin.register(Icon)
# class TemplateAdmin(admin.ModelAdmin):
#     list_display = ['title']

# @admin.register(EkstraContent)
# class TemplateAdmin(admin.ModelAdmin):
#     list_display = ['title']


# @admin.register(EkstraType)
# class TemplateAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     inlines = [ExtraTabularInline]


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
    
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ['template']
    #     else:
    #         return []


admin.site.register(EkstraType, EkstraTypeAdmin)