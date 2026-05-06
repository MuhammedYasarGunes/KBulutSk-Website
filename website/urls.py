from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('galeri/', views.galeri, name='galeri'),
    path('takim/', views.takim, name='takim'),
    path('maclar/', views.maclar, name='maclar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('api/takim/<int:takim_id>/oyuncular/', views.takim_oyuncular_api, name='takim_oyuncular_api'),
    path('yonetim/', views.kulup_yonetimi, name='kulup_yonetimi'),  # ← BU SATIRI EKLE
]
