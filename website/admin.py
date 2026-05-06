from django.contrib import admin
from .models import Oyuncu, Mac, Haber, GaleriÖğesi, Takim

@admin.register(Takim)

class TakimAdmin(admin.ModelAdmin):

    list_display = ("ad",)

    search_fields = ("ad",)
    


@admin.register(Oyuncu)
class OyuncuAdmin(admin.ModelAdmin):
    list_display = ("ad", "takim", "pozisyon", "numara", "olusturma_tarihi")
    list_filter = ("takim", "pozisyon")
    search_fields = ("ad",)


@admin.register(Mac)
class MacAdmin(admin.ModelAdmin):
    list_display = ("takim", "ev_sahibi", "misafir", "ev_sahibi_gol", "misafir_gol", "tarih", "durum")
    list_filter = ("takim", "durum", "lig")
    search_fields = ("ev_sahibi", "misafir")
    date_hierarchy = "tarih"


@admin.register(Haber)
class HaberAdmin(admin.ModelAdmin):
    list_display = ('başlık', 'yayınlama_tarihi', 'güncellenme_tarihi')
    search_fields = ('başlık', 'içerik')
    list_filter = ('yayınlama_tarihi', 'güncellenme_tarihi')
    date_hierarchy = 'yayınlama_tarihi'


@admin.register(GaleriÖğesi)
class GaleriÖğesiAdmin(admin.ModelAdmin):
    list_display = ('id', 'başlık', 'kategori', 'is_video', 'sıra', 'oluşturma_tarihi')
    list_filter = ('kategori', 'oluşturma_tarihi')
    list_editable = ('sıra',)
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('başlık', 'açıklama', 'kategori', 'sıra')
        }),
        ('Medya İçeriği (Resim ve/veya Video)', {
            'fields': ('resim', 'video_dosya', 'video_url'),
            'description': 'Sadece resim yüklerseniz fotoğraf galerisi olur. Video yüklerseniz resim alanı videonun kapak fotoğrafı olarak kullanılır.'
        }),
    )
