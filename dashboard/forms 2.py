from django import forms
from website.models import Haber, Oyuncu, Takim, Mac, GaleriÖğesi, KurucuUye

# Ortak Stil Sınıfı
FORM_CONTROL = {'class': 'form-control'}

class HaberForm(forms.ModelForm):
    class Meta:
        model = Haber
        fields = ['başlık', 'içerik', 'görsel']
        widgets = {
            'başlık': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Haber başlığını giriniz...'}),
            'içerik': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Haber içeriği...'}),
        }

class OyuncuForm(forms.ModelForm):
    class Meta:
        model = Oyuncu
        fields = ['ad', 'takim', 'pozisyon', 'numara']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Oyuncu Adı Soyadı'}),
            'takim': forms.Select(attrs={'class': 'form-control'}),
            'pozisyon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Forvet, Sağ Bek...'}),
            'numara': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Forma No'}),
        }

class TakimForm(forms.ModelForm):
    class Meta:
        model = Takim
        fields = ['ad', 'logo']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Takım/Kategori Adı (Örn: U19 Takımı)'}),
        }

class MacForm(forms.ModelForm):
    class Meta:
        model = Mac
        fields = ['takim', 'ev_sahibi', 'misafir', 'ev_sahibi_gol', 'misafir_gol', 'tarih', 'lig', 'durum']
        widgets = {
            'takim': forms.Select(attrs={'class': 'form-control'}),
            'ev_sahibi': forms.TextInput(attrs={'class': 'form-control'}),
            'misafir': forms.TextInput(attrs={'class': 'form-control'}),
            'ev_sahibi_gol': forms.NumberInput(attrs={'class': 'form-control'}),
            'misafir_gol': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarih': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'lig': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Süper Amatör'}),
            'durum': forms.Select(attrs={'class': 'form-control'}),
        }

class GaleriForm(forms.ModelForm):
    class Meta:
        model = GaleriÖğesi
        # 'turu' alanını fields listesinden çıkardık
        fields = ['başlık', 'açıklama', 'kategori', 'resim', 'video_url', 'video_dosya', 'sıra']
        widgets = {
            'başlık': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opsiyonel başlık'}),
            'açıklama': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'YouTube Linki (Varsa)'}),
            'sıra': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class KurucuUyeForm(forms.ModelForm):
    class Meta:
        model = KurucuUye
        fields = ['ad_soyad', 'unvan', 'gorev', 'telefon', 'foto', 'sira']
        widgets = {
            'ad_soyad': forms.TextInput(attrs={'class': 'form-control'}),
            'unvan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Kulüp Başkanı'}),
            'gorev': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '05xx xxx xx xx'}),
            'sira': forms.NumberInput(attrs={'class': 'form-control'}),
        }