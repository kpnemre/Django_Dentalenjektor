
from django.urls import path
from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('iletisim/', views.contact, name='contact'),
    path('hakkimizda/', views.about, name='about'),
    path('hizmetlerimiz/', views.services, name='services'),
    path('urunlerimiz/', views.products, name='products'),
]