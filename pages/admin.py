from django.contrib import admin
import nested_admin
from .models import *

class AboutContentInline(nested_admin.NestedStackedInline):
    model = AboutContent


class AboutAdmin(nested_admin.NestedModelAdmin):
    inlines = [AboutContentInline]


class ProductContentInline(nested_admin.NestedStackedInline):
    model = ProductContent


class ProductTitleAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProductContentInline]


class HomeMiddleDetailInline(nested_admin.NestedStackedInline):
    model = HomeMiddleDetail


class HomeMiddleHeaderAdmin(nested_admin.NestedModelAdmin):
    inlines = [HomeMiddleDetailInline]

# admin.site.register(HomeMiddleDetail)
admin.site.register(HomeMiddleHeader, HomeMiddleHeaderAdmin)
admin.site.register(Home)
admin.site.register(HomeDetail)

admin.site.register(HomeFooterUp)

admin.site.register(Setting)
admin.site.register(ContactInfo)
admin.site.register(About, AboutAdmin)
admin.site.register(Services)
admin.site.register(ProductTitle,ProductTitleAdmin)
# admin.site.register(ProductContent)

# admin.site.register(About)
# admin.site.register(AboutContent)

