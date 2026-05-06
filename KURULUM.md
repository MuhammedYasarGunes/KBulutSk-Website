# Django Projesi Kurulum Yönergeleri

Bu belgede Karabağlar Atletik FK Django web sitesinin nasıl kurulacağı ve çalıştırılacağı açıklanmıştır.

## Hızlı Başlangıç (Yerel Geliştirme)

### 1. Terminal'de projeye gir
```bash
cd /Users/shzany/Projects/KarabağlarAtletik
```

### 2. Sanal ortamı etkinleştir (henüz yapmadıysan)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Bağımlılıkları yükle
```bash
pip install -r requirements.txt
```

### 4. .env dosyasını oluştur
```bash
cp .env.example .env
# Gerekirse .env dosyasını düzenle
```

### 5. Veritabanını hazırla
```bash
python manage.py migrate
```

### 6. Admin kullanıcı oluştur (isteğe bağlı)
```bash
python manage.py createsuperuser
```

### 7. Static dosyaları topla
```bash
python manage.py collectstatic --noinput
```

### 8. Geliştirme sunucusunu başlat
```bash
python manage.py runserver
```

Tarayıcında aç: **http://localhost:8000**
Admin paneli: **http://localhost:8000/admin**

## Proje Yapısı

```
KarabağlarAtletik/
├── karabaglar_project/          # Django proje ayarları
│   ├── settings.py              # Proje konfigürasyonu
│   ├── urls.py                  # URL yönlendirmesi
│   ├── wsgi.py                  # Production server
│   └── asgi.py                  # Async server
│
├── website/                      # Ana Django app
│   ├── models.py                # Veritabanı modelleri (Oyuncu, Maç, Haber)
│   ├── views.py                 # İş mantığı
│   ├── urls.py                  # App URL'leri
│   ├── admin.py                 # Admin paneli ayarları
│   ├── apps.py                  # App konfigürasyonu
│   ├── tests.py                 # Birim testleri
│   │
│   ├── templates/               # HTML şablonları
│   │   ├── base.html            # Temel şablon
│   │   ├── index.html           # Ana sayfa (slider, haberler)
│   │   ├── galeri.html          # Galeri sayfası
│   │   ├── takim.html           # Takım sayfası
│   │   ├── maclar.html          # Maçlar sayfası
│   │   └── iletisim.html        # İletişim sayfası
│   │
│   ├── static/                  # Statik dosyalar
│   │   ├── css/
│   │   │   └── style.css        # Tüm tasarım
│   │   ├── js/
│   │   │   └── script.js        # JavaScript kodu
│   │   └── img/                 # Resimler
│   │
│   └── migrations/              # Veritabanı migrasyonları
│
├── manage.py                    # Django yönetim aracı
├── requirements.txt             # Python paketleri
├── .env.example                 # Ortam değişkenleri şablonu
├── .gitignore                   # Git görmezden gelecek dosyalar
├── setup.sh                     # Otomatik kurulum betiği
├── Dockerfile                   # Docker imajı
├── docker-compose.yml           # Docker Compose yapılandırması
├── Procfile                     # Heroku deployment
├── README.md                    # Proje açıklaması
└── DEPLOYMENT.md                # Production deployment rehberi
```

## Sayfalar ve Fonksiyonlar

### Ana Sayfa (/)
- **Slider:** 3 slide'lı otomatik oynatılan hero slider
- **Haberler:** Yatay kaydırmalı haber kartları
- **Footer:** Linkler ve copyright

### Galeri (/galeri/)
- **Filtre:** Maçlar, Antrenman, Etkinlikler kategorileri
- **Grid Layout:** 3 sütun (masaüstü), 2 sütun (tablet), 1 sütun (mobil)
- **Hover Efektleri:** Görsel ve metin animasyonları

### Takım (/takim/)
- **Oyuncu Kartları:** 3x3 grid layout
- **İstatistikler:** Takım istatistikleri
- **Admin Yönetimi:** Django admin'den oyuncu ekle/düzenle

### Maçlar (/maclar/)
- **Maç Kartları:** Tarih, takımlar, skorlar
- **Durumlar:** Kazanıldı (cyan), Berabere (sarı), Kaybedildi (kırmızı), Gelecek (mavi)
- **Sezon İstatistikleri:** 6 adet istatistik kutusu

### İletişim (/iletisim/)
- **İletişim Bilgileri:** Adres, telefon, email
- **İletişim Formu:** Ad, email, konu, mesaj
- **Sosyal Medya:** Linkler
- **Konum Haritası:** Google Maps placeholder

## Admin Paneli Kullanımı

URL: `http://localhost:8000/admin`

### Oyuncu Yönetimi
```
Admin → Oyuncular → Oyuncu Ekle
- Ad Soyad
- Pozisyon
- Jersey Numarası
```

### Maç Yönetimi
```
Admin → Maçlar → Maç Ekle
- Tarih
- Ev Sahibi Takımı
- Misafir Takımı
- Ev Sahibi Gol
- Misafir Gol
- Lig
- Durum (Kazanıldı/Berabere/Kaybedildi/Gelecek)
```

### Haber Yönetimi
```
Admin → Haberler → Haber Ekle
- Başlık
- İçerik
- Görsel (isteğe bağlı)
- Yayınlama tarihi
```

## Docker ile Çalıştırma

### Docker Compose (En Kolay)
```bash
docker-compose up -d
```

Erişim: http://localhost:8000

### Manuel Docker
```bash
# İmaj inşa et
docker build -t karabaglar-atletik .

# Konteyner çalıştır
docker run -p 8000:8000 karabaglar-atletik
```

## Production Deployment

### Heroku'ya Deploy
```bash
# Heroku CLI yükle
# https://devcenter.heroku.com/articles/heroku-cli

# Giriş yap
heroku login

# Uygulama oluştur
heroku create karabaglar-atletik

# Environment değişkenlerini ayarla
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy et
git push heroku main
```

### VPS'e Deploy (DigitalOcean, AWS, Azure, vb.)

#### Server Hazırlığı (Ubuntu 22.04)
```bash
# SSH ile bağlan
ssh root@your_server_ip

# Sistem paketlerini güncelle
apt update && apt upgrade -y

# Python ve gerekli araçları yükle
apt install -y python3.11 python3.11-venv python3-pip nginx postgresql

# Projeyi kopyala
git clone your-repo-url /var/www/karabaglar
cd /var/www/karabaglar

# Sanal ortamı oluştur
python3.11 -m venv venv
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# .env dosyasını oluştur
cp .env.example .env
# .env dosyasını düzenle (SECRET_KEY, DEBUG, vb.)

# Migrasyonları çalıştır
python manage.py migrate

# Static dosyaları topla
python manage.py collectstatic --noinput

# Nginx konfigürasyonu oluştur
# (Özel yapılandırma gerekli)

# Gunicorn başlat
gunicorn karabaglar_project.wsgi --bind 0.0.0.0:8000
```

Daha detaylı deployment rehberi: [DEPLOYMENT.md](DEPLOYMENT.md)

## Önemli Ortam Değişkenleri

`.env` dosyasında ayarla:

```
# Django Ayarları
SECRET_KEY=your-very-secret-key-here
DEBUG=False  # Production için False!
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (varsayılan SQLite)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# Email (isteğe bağlı)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Sık Sorunlar ve Çözümleri

### "Port 8000 zaten kullanımda" hatası
```bash
# Farklı port kullan
python manage.py runserver 8001
```

### Static dosyaları yüklenmiyorsa
```bash
# Static dosyaları yeniden topla
python manage.py collectstatic --clear --noinput
```

### Database hatası
```bash
# Veritabanını sıfırla (YAZILI VERİ KAYBOLACAK!)
python manage.py flush

# Migrasyonları yeniden çalıştır
python manage.py migrate
```

### Admin paneline erişilemiyor
```bash
# Admin kullanıcı oluştur/sıfırla
python manage.py createsuperuser
```

## Testler Çalıştırma

```bash
# Tüm testleri çalıştır
python manage.py test

# Belirli test çalıştır
python manage.py test website.tests.WebsiteViewsTestCase.test_index_page_loads
```

## Geliştirme Tüyoları

### Debug Mode İçin Detaylı Hata Bilgisi
```python
# settings.py'da DEBUG = True olduğunda hata detayları görünür
```

### Database Sorguları İnceleme
```python
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as ctx:
    # Kodunuz burada
    pass
print(ctx.captured_queries)  # SQL sorgularını göster
```

### Django Shell
```bash
python manage.py shell

# Shell'de Python kodu çalıştır
>>> from website.models import Oyuncu
>>> oyuncular = Oyuncu.objects.all()
>>> oyuncular.count()
```

## Güvenlik Kontrol Listesi

- [ ] `SECRET_KEY` değiştirildi mi?
- [ ] `DEBUG = False` (production'da)
- [ ] `ALLOWED_HOSTS` güncellendi mi?
- [ ] HTTPS etkinleştirildi mi?
- [ ] Database şifresi güçlü mü?
- [ ] Admin paneli URL değiştirildi mi?
- [ ] Regular backups yapılıyor mu?
- [ ] Django güncellemeleri kontrol ediliyor mu?

## Faydalı Kaynaklar

- [Django Resmi Dokümantasyonu](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/5.0/topics/db/models/)
- [Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)

## İletişim ve Destek

Sorularınız olursa, iletişim formundan bizimle iletişime geçin!

---

**Son Güncelleme:** 20 Nisan 2026
**Django Sürümü:** 5.0.3
**Python Sürümü:** 3.11+
