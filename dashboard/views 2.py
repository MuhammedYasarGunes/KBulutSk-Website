from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from website.models import Takim, Oyuncu, Mac, Haber, GaleriÖğesi, KurucuUye

# FORMLARI İMPORT EDİYORUZ
from .forms import (
    HaberForm, OyuncuForm, TakimForm, 
    MacForm, GaleriForm, KurucuUyeForm
)

# ==========================================
# 1. LİSTELEME GÖRÜNÜMLERİ (READ)
# ==========================================

@login_required
def index(request):
    """Dashboard Ana Sayfası - Kulüp Özeti"""
    context = {
        'toplam_oyuncu': Oyuncu.objects.count(),
        'toplam_takim': Takim.objects.count(),
        'yaklasan_mac_sayisi': Mac.objects.filter(durum='gelecek').count(),
        'toplam_haber': Haber.objects.count(),
        'yaklasan_maclar': Mac.objects.filter(durum='gelecek').order_by('tarih')[:5],
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def takimlar_yonetimi(request):
    takimlar = Takim.objects.all()
    return render(request, 'dashboard/takimlar.html', {'takimlar': takimlar})

@login_required
def oyuncular_yonetimi(request):
    oyuncular = Oyuncu.objects.all().select_related('takim').order_by('-olusturma_tarihi')
    return render(request, 'dashboard/oyuncular.html', {'oyuncular': oyuncular})

@login_required
def maclar_yonetimi(request):
    maclar = Mac.objects.all().select_related('takim').order_by('-tarih')
    return render(request, 'dashboard/maclar.html', {'maclar': maclar})

@login_required
def galeri_yonetimi(request):
    ogeler = GaleriÖğesi.objects.all().order_by('-oluşturma_tarihi')
    return render(request, 'dashboard/galeri.html', {'ogeler': ogeler})

@login_required
def haberler_yonetimi(request):
    haberler = Haber.objects.all().order_by('-yayınlama_tarihi')
    return render(request, 'dashboard/haberler.html', {'haberler': haberler})


# ==========================================
# 2. EKLEME FONKSİYONLARI (CREATE)
# ==========================================

@login_required
def haber_ekle(request):
    if request.method == 'POST':
        form = HaberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Haber başarıyla yayınlandı.")
            return redirect('dashboard:haberler')
    else:
        form = HaberForm()
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Yeni Haber Ekle'})

@login_required
def oyuncu_ekle(request):
    if request.method == 'POST':
        form = OyuncuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Oyuncu kadroya başarıyla eklendi.")
            return redirect('dashboard:oyuncular')
    else:
        form = OyuncuForm()
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Yeni Oyuncu Ekle'})

@login_required
def takim_ekle(request):
    if request.method == 'POST':
        form = TakimForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Yeni takım başarıyla oluşturuldu.")
            return redirect('dashboard:takimlar')
    else:
        form = TakimForm()
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Yeni Takım Ekle'})

@login_required
def mac_ekle(request):
    if request.method == 'POST':
        form = MacForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Maç fikstüre eklendi.")
            return redirect('dashboard:maclar')
    else:
        form = MacForm()
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Yeni Maç Ekle'})

@login_required
def galeri_ekle(request):
    if request.method == 'POST':
        baslik = request.POST.get('baslik', '').strip() # Başlığı formdan alıyoruz (boşsa boş string olur)
        kategori = request.POST.get('kategori', 'maçlar')
        youtube_url = request.POST.get('video_url', '').strip()
        
        # 1. DURUM: Youtube Linki Eklendiyse
        if youtube_url:
            GaleriÖğesi.objects.create(
                başlık=baslik if baslik else None, # Eğer başlık girildiyse kaydet, girilmediyse boş (None) bırak
                kategori=kategori,
                video_url=youtube_url
            )
            messages.success(request, "YouTube videosu galeriye eklendi.")
            return redirect('dashboard:galeri')

        # 2. DURUM: Dosya Yüklendiyse (Toplu Yükleme)
        dosyalar = request.FILES.getlist('medyalar')
        
        if dosyalar:
            basarili_sayi = 0
            hata_sayi = 0

            for dosya in dosyalar:
                try:
                    dosya.seek(0) 

                    if dosya.content_type.startswith('video/'):
                        GaleriÖğesi.objects.create(başlık=baslik if baslik else None, kategori=kategori, video_dosya=dosya)
                    else:
                        GaleriÖğesi.objects.create(başlık=baslik if baslik else None, kategori=kategori, resim=dosya)
                        
                    basarili_sayi += 1
                    
                except Exception as e:
                    print(f"HATA - {dosya.name} yüklenemedi: {str(e)}") 
                    hata_sayi += 1

            if basarili_sayi > 0:
                messages.success(request, f"{basarili_sayi} adet medya başarıyla galeriye eklendi.")
            if hata_sayi > 0:
                messages.error(request, f"{hata_sayi} adet medya yüklenemedi. (Dosya bozuk olabilir)")
                
            return redirect('dashboard:galeri')
            
        messages.warning(request, "Lütfen bir dosya yükleyin veya YouTube linki girin.")

    return render(request, 'dashboard/galeri_ekle.html')

@login_required
def kurucu_uye_ekle(request):
    if request.method == 'POST':
        form = KurucuUyeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Kurucu üye sisteme eklendi.")
            return redirect('dashboard:index')
    else:
        form = KurucuUyeForm()
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Yeni Kurucu Üye Ekle'})


# ==========================================
# 3. SİLME FONKSİYONLARI (DELETE)
# ==========================================

@login_required
def haber_sil(request, pk):
    obj = get_object_or_404(Haber, pk=pk)
    obj.delete()
    messages.warning(request, "Haber silindi.")
    return redirect('dashboard:haberler')

@login_required
def oyuncu_sil(request, pk):
    obj = get_object_or_404(Oyuncu, pk=pk)
    obj.delete()
    messages.warning(request, "Oyuncu kaydı silindi.")
    return redirect('dashboard:oyuncular')

@login_required
def takim_sil(request, pk):
    obj = get_object_or_404(Takim, pk=pk)
    obj.delete()
    messages.warning(request, "Takım ve bağlı tüm veriler silindi.")
    return redirect('dashboard:takimlar')

@login_required
def mac_sil(request, pk):
    obj = get_object_or_404(Mac, pk=pk)
    obj.delete()
    messages.warning(request, "Maç kaydı fikstürden kaldırıldı.")
    return redirect('dashboard:maclar')

@login_required
def galeri_sil(request, pk):
    obj = get_object_or_404(GaleriÖğesi, pk=pk)
    obj.delete()
    messages.warning(request, "Medya dosyası galeriden silindi.")
    return redirect('dashboard:galeri')

@login_required
def kurucu_uye_sil(request, pk):
    obj = get_object_or_404(KurucuUye, pk=pk)
    obj.delete()
    messages.warning(request, "Yönetim kurulu üyesi silindi.")
    return redirect('dashboard:index')
# --- DÜZENLEME (UPDATE) FONKSİYONLARI ---

@login_required
def haber_duzenle(request, pk):
    obj = get_object_or_404(Haber, pk=pk)
    if request.method == 'POST':
        form = HaberForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Haber başarıyla güncellendi.")
            return redirect('dashboard:haberler')
    else:
        form = HaberForm(instance=obj)
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Haberi Düzenle'})

@login_required
def oyuncu_duzenle(request, pk):
    obj = get_object_or_404(Oyuncu, pk=pk)
    if request.method == 'POST':
        form = OyuncuForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Oyuncu bilgileri güncellendi.")
            return redirect('dashboard:oyuncular')
    else:
        form = OyuncuForm(instance=obj)
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Oyuncuyu Düzenle'})

@login_required
def takim_duzenle(request, pk):
    obj = get_object_or_404(Takim, pk=pk)
    if request.method == 'POST':
        form = TakimForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Takım bilgileri güncellendi.")
            return redirect('dashboard:takimlar')
    else:
        form = TakimForm(instance=obj)
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Takımı Düzenle'})

@login_required
def mac_duzenle(request, pk):
    obj = get_object_or_404(Mac, pk=pk)
    if request.method == 'POST':
        form = MacForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Maç bilgileri güncellendi.")
            return redirect('dashboard:maclar')
    else:
        form = MacForm(instance=obj)
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Maçı Düzenle'})

@login_required
def galeri_duzenle(request, pk):
    obj = get_object_or_404(GaleriÖğesi, pk=pk)
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Medya bilgileri güncellendi.")
            return redirect('dashboard:galeri')
    else:
        form = GaleriForm(instance=obj)
    return render(request, 'dashboard/form_sayfasi.html', {'form': form, 'baslik': 'Medyayı Düzenle'})
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

@require_POST # Sadece form gönderilince çalışır, güvenlidir
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')
