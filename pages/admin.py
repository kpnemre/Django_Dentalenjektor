from django.contrib import admin
import nested_admin
from .models import *

class AboutContentInline(nested_admin.NestedStackedInline):
    model = AboutContent


class AboutAdmin(nested_admin.NestedModelAdmin):
    inlines = [AboutContentInline]



admin.site.register(HomeMiddleDetail)
admin.site.register(HomeMiddleHeader)
admin.site.register(Home)
admin.site.register(HomeDetail)
admin.site.register(HomeIcon)
admin.site.register(HomeFooterUp)
admin.site.register(Icon)
admin.site.register(Setting)
admin.site.register(ContactInfo)
admin.site.register(About, AboutAdmin)
admin.site.register(Services)

# admin.site.register(About)
# admin.site.register(AboutContent)

