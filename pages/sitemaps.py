from django.contrib.sitemaps import Sitemap
from django.urls import reverse



class StaticViewSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return ['pages:home', 'pages:about', 'pages:contact', 'pages:services', 'pages:products']

    def location(self, item):
        return reverse(item)