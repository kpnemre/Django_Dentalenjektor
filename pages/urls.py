
from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    # path('<slug:slug>/', views.header_detail, name='header-detail'),
    # path('<slug:slug>/', views.page_detail, name='detail'),
    

]