from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Login işlemi için Django'nun hazır view'ını çekiyoruz

app_name = 'dashboard'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Ana Sayfa
    path('', views.index, name='index'),

    # HABERLER
    path('haberler/', views.haberler_yonetimi, name='haberler'),
    path('haberler/ekle/', views.haber_ekle, name='haber_ekle'),
    path('haberler/sil/<int:pk>/', views.haber_sil, name='haber_sil'),

    # OYUNCULAR
    path('oyuncular/', views.oyuncular_yonetimi, name='oyuncular'),
    path('oyuncular/ekle/', views.oyuncu_ekle, name='oyuncu_ekle'),
    path('oyuncular/sil/<int:pk>/', views.oyuncu_sil, name='oyuncu_sil'),

    # TAKIMLAR
    path('takimlar/', views.takimlar_yonetimi, name='takimlar'),
    path('takimlar/ekle/', views.takim_ekle, name='takim_ekle'), # Eklendi
    path('takimlar/sil/<int:pk>/', views.takim_sil, name='takim_sil'),

    # MAÇLAR
    path('maclar/', views.maclar_yonetimi, name='maclar'),
    path('maclar/ekle/', views.mac_ekle, name='mac_ekle'), # Eklendi
    path('maclar/sil/<int:pk>/', views.mac_sil, name='mac_sil'),

    # GALERİ
    path('galeri/', views.galeri_yonetimi, name='galeri'),
    path('galeri/ekle/', views.galeri_ekle, name='galeri_ekle'), # Eklendi
    path('galeri/sil/<int:pk>/', views.galeri_sil, name='galeri_sil'),

    # KURUCU ÜYELER (YÖNETİM)
    path('yonetim/ekle/', views.kurucu_uye_ekle, name='kurucu_uye_ekle'), # Eklendi
    path('yonetim/sil/<int:pk>/', views.kurucu_uye_sil, name='kurucu_uye_sil'),
    path('haberler/duzenle/<int:pk>/', views.haber_duzenle, name='haber_duzenle'),
path('oyuncular/duzenle/<int:pk>/', views.oyuncu_duzenle, name='oyuncu_duzenle'),
path('takimlar/duzenle/<int:pk>/', views.takim_duzenle, name='takim_duzenle'),
path('maclar/duzenle/<int:pk>/', views.mac_duzenle, name='mac_duzenle'),
path('galeri/duzenle/<int:pk>/', views.galeri_duzenle, name='galeri_duzenle'),
]