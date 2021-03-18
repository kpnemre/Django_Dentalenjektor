
from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('iletisim/', views.contact, name='contact'),
    path('hakkimizda/', views.about, name='about'),
    path('hizmetler/', views.services, name='services'),
    path('products/', views.products, name='products'),
    # path('<slug:slug>/', views.header_detail, name='header-detail'),
    # path('<slug:slug>/', views.page_detail, name='detail'),
    

]