from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class GaleryTabularAdmin(admin.TabularInline):
    model = Galery


@admin.register(Page)
class OrderAdmin(admin.ModelAdmin):
    inlines = [GaleryTabularAdmin]
    list_display = ['title']


@admin.register(Header)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title']

