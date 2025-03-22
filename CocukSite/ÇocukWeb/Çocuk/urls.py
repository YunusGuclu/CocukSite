from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('yemek-tarifleri/', views.yemek_tarifleri, name='yemek_tarifleri'),
    path('el-sanatlari/', views.el_sanatlari, name='el_sanatlari'),
    path('bilmeceler/', views.bilmeceler, name='bilmeceler'),
    path('hikayeler/', views.hikayeler, name='hikayeler'),
    
    # Detay sayfaları
    path('aktivite/<int:id>/', views.aktivite_detay, name='aktivite_detay'),
    path('deney/<int:id>/', views.deney_detay, name='deney_detay'),
    path('el-sanati/<int:id>/', views.el_sanati_detay, name='el_sanati_detay'),
    path('yemek/<int:id>/', views.yemek_detay, name='yemek_detay'),
    path('doga/<int:id>/', views.doga_detay, name='doga_detay'),
]