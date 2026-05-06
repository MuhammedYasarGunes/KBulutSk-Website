from django.db import models
from cloudinary.models import CloudinaryField


class Takim(models.Model):
    ad = models.CharField(max_length=200)
    logo = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.ad


class Oyuncu(models.Model):
    takim = models.ForeignKey(Takim, on_delete=models.CASCADE, related_name="oyuncular")

    ad = models.CharField(max_length=100)
    pozisyon = models.CharField(max_length=50)
    numara = models.IntegerField()

    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad} - #{self.numara}"


class Mac(models.Model):
    STATUS_CHOICES = [
        ('kazanildi', 'Kazanıldı'),
        ('berabere', 'Berabere'),
        ('kaybedildi', 'Kaybedildi'),
        ('gelecek', 'Gelecek'),
    ]

    takim = models.ForeignKey(Takim, on_delete=models.CASCADE, related_name="maclar")

    ev_sahibi = models.CharField(max_length=100)
    misafir = models.CharField(max_length=100)

    ev_sahibi_gol = models.IntegerField(default=0)
    misafir_gol = models.IntegerField(default=0)

    tarih = models.DateTimeField()
    lig = models.CharField(max_length=100)
    durum = models.CharField(max_length=20, choices=STATUS_CHOICES, default='gelecek')

    def __str__(self):
        return f"{self.ev_sahibi} vs {self.misafir}"


class Haber(models.Model):
    başlık = models.CharField(max_length=200)
    içerik = models.TextField()
    görsel = CloudinaryField('image', blank=True, null=True)

    yayınlama_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-yayınlama_tarihi']

    def __str__(self):
        return self.başlık


class GaleriÖğesi(models.Model):
    KATEGORI_CHOICES = [
        ('maçlar', 'Maçlar'),
        ('antrenman', 'Antrenman'),
        ('etkinlik', 'Etkinlikler'),
    ]

    # Başlık zorunlu değil, toplu yüklemede otomatik atanabilir
    başlık = models.CharField(max_length=200, blank=True, null=True)
    açıklama = models.TextField(blank=True)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES, default='maçlar')

    # Eğer video eklersen, bu resim videonun kapak fotoğrafı olur!
    resim = CloudinaryField('image', blank=True, null=True) 
    
    # Videolar için iki farklı seçenek
    video_dosya = CloudinaryField(resource_type="video", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube veya başka bir video linki")

    oluşturma_tarihi = models.DateTimeField(auto_now_add=True)
    sıra = models.IntegerField(default=0)

    class Meta:
        ordering = ['-sıra', '-oluşturma_tarihi']

    def __str__(self):
        return self.başlık if self.başlık else f"Galeri Öğesi #{self.id}"

    # --- AKILLI KONTROLLER ---
    @property
    def is_video(self):
        # Dosya veya link varsa bu bir videodur
        return bool(self.video_dosya or self.video_url)

    @property
    def has_youtube_video(self):
        # Eğer video_url boşsa (None ise) hiç kontrol etmeden direkt False dön
        if not self.video_url:
            return False
        
        # Eğer doluysa içinde youtube geçiyor mu diye bak
        return "youtube.com" in self.video_url or "youtu.be" in self.video_url
     
class KurucuUye(models.Model):
    ad_soyad = models.CharField(max_length=120)
    unvan    = models.CharField(max_length=80,   help_text="Başkan, Sekreter…")
    gorev    = models.CharField(max_length=120,  blank=True)
    telefon  = models.CharField(max_length=20)
    foto     = models.ImageField(upload_to='yonetim/', blank=True, null=True)
    sira     = models.PositiveSmallIntegerField(default=0)
 
    class Meta:
        ordering = ['sira']
        verbose_name = 'Kurucu Üye'
        verbose_name_plural = 'Kurucu Üyeler'
 
    def __str__(self):
        return self.ad_soyad