<<<<<<< HEAD
# 🏀 K.Bulut Spor Kulübü - Web Sitesi

<!-- Add Banner/Hero Image Here -->
![K.Bulut Spor Kulübü Banner](<!-- ADD_YOUR_BANNER_IMAGE_URL_HERE -->)

> K.Bulut Spor Kulübü'nün modern, tamamen responsive web uygulaması. Oyuncu yönetimi, maç takibi, haberler ve galeri özelliklerini içerir.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.14-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## ✨ Özellikler

- 🎯 **Takım Yönetimi** - Oyuncular, takımlar ve pozisyonlar
- 🏆 **Maç Takibi** - Maçlar, sonuçlar ve istatistikler
- 📰 **Haberler** - Son haberleri takip edin
- 🖼️ **Galeri** - Etkinlik fotoğrafları ve videolar
- 📊 **Admin Dashboard** - Tamamen donanımlı yönetim paneli
- 🌐 **Responsive Design** - Tüm cihazlarda mükemmel görünüm
- ☁️ **Cloudinary Integration** - Bulut tabanlı medya yönetimi
- 🐳 **Docker Support** - Kolay deployment ve containerization
- 📱 **Mobil Optimized** - Smartphones, tablets ve desktoplar

---

## 🛠️ Teknoloji Stack

| Kategori | Teknoloji |
|----------|-----------|
| **Backend** | Django 5.0 |
| **Runtime** | Python 3.10+ |
| **Database** | PostgreSQL 14+ |
| **Media Storage** | Cloudinary |
| **Web Server** | Gunicorn |
| **Static Files** | WhiteNoise |
| **Containerization** | Docker & Docker Compose |
| **Deployment** | Railway / Heroku |
| **ORM** | Django ORM |
| **Authentication** | Django Auth |

---

## 📋 Gereksinimler

- Python 3.10 veya daha yüksek
- PostgreSQL 14 veya daha yüksek
- pip (Python paket yöneticisi)
- Cloudinary hesabı (opsiyonel, resim depolaması için)
- Git

---

## 🚀 Hızlı Başlangıç

### 1. Projeyi Clone Edin

```bash
git clone https://github.com/yourusername/K.BulutSK-Website.git
cd K.BulutSK-Website
```

### 2. Virtual Environment Oluşturun

```bash
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
# veya
venv\Scripts\activate  # Windows
```

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Environment Değişkenlerini Ayarlayın

`.env` dosyası oluşturun ve aşağıdaki içeriği ekleyin:

```env
# Django
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/K.Bulutsk_db

# Cloudinary (Opsiyonel)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

### 5. Veritabanını Hazırlayın

```bash
python manage.py migrate
python manage.py createsuperuser  # Admin kullanıcı oluştur
python manage.py collectstatic --noinput  # Static dosyaları topla
```

### 6. Development Sunucusunu Çalıştırın

```bash
python manage.py runserver
```

Tarayıcınızda açın: **http://localhost:8000**  
Admin paneli: **http://localhost:8000/admin**

---

## 📁 Proje Yapısı

```
K.BulutSK-Website/
├── dashboard/                 # Admin Dashboard Uygulaması
│   ├── models.py             # Veritabanı modelleri
│   ├── views.py              # Dashboard views
│   ├── urls.py               # URL routeları
│   ├── forms.py              # Django formları
│   ├── templates/            # HTML template'leri
│   │   └── dashboard/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── galeri.html
│   │       ├── haberler.html
│   │       ├── maclar.html
│   │       ├── oyuncular.html
│   │       └── takimlar.html
│   └── migrations/           # Veritabanı migrasyonları
│
├── website/                   # Genel Website Uygulaması
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/            # Web sayfası template'leri
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── galeri.html
│   │   ├── maclar.html
│   │   ├── takim.html
│   │   └── iletisim.html
│   ├── static/               # CSS, JS, resimler
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── migrations/
│
├── karabaglar_project/       # Django Proje Ayarları
│   ├── settings.py           # Proje konfigürasyonu
│   ├── urls.py               # Ana URL konfigürasyonu
│   ├── wsgi.py               # Production WSGI
│   └── asgi.py               # Async ASGI
│
├── staticfiles/              # Toplanan static dosyalar
├── manage.py                 # Django yönetim komutu
├── requirements.txt          # Python bağımlılıkları
├── Dockerfile                # Docker konteyner konfigürasyonu
├── docker-compose.yml        # Multi-container orchestration
├── Procfile                  # Heroku/Railway deployment
├── runtime.txt               # Python runtime versiyonu
└── README.md                 # Bu dosya
```

---

## 🗄️ Veritabanı Modelleri

### Ana Modeller:

```
Oyuncu (Player)
  ├── Adı, Soyadı
  ├── Pozisyon
  ├── Dorsal Numarası
  └── Profil Fotoğrafı

Takım (Team)
  ├── Takım Adı
  ├── Liği
  ├── Oyuncular (Foreign Key)
  └── Logo

Maç (Match)
  ├── Tarih
  ├── Ev Sahibi Takım
  ├── Konuk Takım
  ├── Skor
  └── Maç Detayları

Haber (News)
  ├── Başlık
  ├── İçerik
  ├── Yayınlanma Tarihi
  └── Kapak Fotoğrafı

Galeri (Gallery)
  ├── Etkinlik Adı
  ├── Açıklama
  ├── Fotoğraflar
  └── Yükleme Tarihi
```

---

## ☁️ Cloudinary Konfigürasyonu

Resim yönetimi için Cloudinary kullanılmaktadır:

### Adım 1: Cloudinary Hesabı Oluşturun
[Cloudinary'ye git](https://cloudinary.com/) ve ücretsiz hesap oluşturun.

### Adım 2: API Credentials'ı Alın
Dashboard'dan:
- Cloud Name
- API Key
- API Secret

### Adım 3: Environment'a Ekleyin
```env
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

**Mevcut Cloudinary özellikleri:**
- Otomatik resim optimizasyonu
- CDN üzerinden hızlı dağıtım
- Bandwidth yönetimi
- Resim transformasyonları

---

## 🐳 Docker ile Çalıştırma

### Tüm Servisleri Başlat

=======
<<<<<<< HEAD
# K.Bulut FK - Django Web Sitesi

K.Bulut FK'nin tam özellikli Django web sitesi uygulaması.

## Özellikler

✅ **Responsive Tasarım** - Tüm cihazlar için optimize edilmiş
✅ **Slider** - Otomatik oynatılan hero slider
✅ **Galeri** - Filtreli resim galerisi
✅ **Takım Sayfası** - Oyuncu kartları ve istatistikleri
✅ **Maçlar Sayfası** - Sezon maçları ve sonuçları
✅ **İletişim Formu** - Ziyaretçi mesajları için
✅ **Admin Paneli** - Django admin ile kolay yönetim
✅ **Database Modeller** - Oyuncu, Maç, Haber yönetimi

## Teknoloji Stack

- **Backend:** Django 5.0.3
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite (development), PostgreSQL (production)
- **Server:** Gunicorn + Nginx
- **Containerization:** Docker & Docker Compose

## Hızlı Başlangıç

### Yerel Geliştirme
```bash
# 1. Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# 2. Bağımlılıkları yükle
pip install -r requirements.txt

# 3. Migrasyonları çalıştır
python manage.py migrate

# 4. Sunucuyu başlat
python manage.py runserver
```

Tarayıcıda: http://localhost:8000

### Docker ile
>>>>>>> 60e271c705f5d58f95bab4e10c1e29a1bde0bd73
```bash
docker-compose up -d
```

<<<<<<< HEAD
### Veritabanını Hazırla
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Servisler:
- **Web**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **Admin Panel**: http://localhost:8000/admin

### Container'ı Durdur
```bash
docker-compose down
```

---

## 🌐 Deployment

### Railway'e Deploy Etme

1. **Railway Hesabı Oluşturun**: [railway.app](https://railway.app)

2. **GitHub'da Push Edin**:
```bash
git push origin main
```

3. **Railway Projesi Bağlayın**:
   - Railway'de yeni proje oluşturun
   - GitHub repo'sunu bağlayın
   - Environment variables ekleyin

4. **Environment Variables**:
```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourapp.up.railway.app
DATABASE_URL=postgresql://... (Railway tarafından sağlanır)
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
```

**Üretim URL**: [K.Bulutspor.up.railway.app](https://K.Bulutspor.up.railway.app)

---

## 📸 Screenshot'lar

### Ana Sayfa
<!-- Add screenshot of homepage -->
![Ana Sayfa](<!-- ADD_HOMEPAGE_SCREENSHOT_URL -->)

### Admin Dashboard
<!-- Add screenshot of admin panel -->
![Admin Dashboard](<!-- ADD_ADMIN_SCREENSHOT_URL -->)

### Galeri Sayfası
<!-- Add screenshot of gallery -->
![Galeri](<!-- ADD_GALLERY_SCREENSHOT_URL -->)

### Mobil Görünüm
<!-- Add screenshot of mobile view -->
![Mobil Görünüm](<!-- ADD_MOBILE_SCREENSHOT_URL -->)

---

## 🔧 Development Komutları

```bash
# Yeni migration oluştur
python manage.py makemigrations

# Migration uygula
python manage.py migrate

# Admin kullanıcı oluştur
python manage.py createsuperuser

# Django shell (interaktif Python)
python manage.py shell

# Static dosyaları topla
python manage.py collectstatic

# Sunucuyu çalıştır
python manage.py runserver

# Tests çalıştır
python manage.py test

# Galeri optimizasyonunu kontrol et
python validate_gallery_optimization.py
```

---

## 📝 Veritabanı Backup ve Restore

### PostgreSQL Backup
```bash
pg_dump -U user -h localhost K.Bulutsk_db > backup.sql
```

### Restore İşlemi
```bash
psql -U user -h localhost K.Bulutsk_db < backup.sql
```

---

## 🐛 Sorun Giderme

### Problem: "DATABASE_URL not found"
**Çözüm**: `.env` dosyasını proje root'una ekleyin

### Problem: "Cloudinary credentials missing"
**Çözüm**: Environment variables'ı kontrol edin

### Problem: Statik dosyalar yüklenmiyor
**Çözüm**: `python manage.py collectstatic --noinput` komutunu çalıştırın

### Problem: Admin paneline erişilemiyor
**Çözüm**: `python manage.py createsuperuser` komutunu çalıştırın

---

## 📚 Kullanılan Kütüphaneler

| Kütüphane | Versiyon | Amaç |
|-----------|----------|------|
| Django | 5.0.14 | Web Framework |
| psycopg | latest | PostgreSQL Adapter |
| Pillow | 10.4.0 | Resim İşleme |
| Cloudinary | 1.44.2 | Bulut Medya Depolaması |
| django-cloudinary-storage | 0.3.0 | Cloudinary Storage Backend |
| Gunicorn | 21.2.0 | WSGI HTTP Server |
| WhiteNoise | 6.6.0 | Static File Serving |
| python-dotenv | 1.0.1 | Environment Variables |

---

## 🤝 Katkıda Bulunma

Katkılarınız hoş geldiniz! Lütfen aşağıdaki adımları takip edin:

1. **Fork** yapın
2. Feature branch'i oluşturun: `git checkout -b feature/AmazingFeature`
3. Değişiklikleri commit edin: `git commit -m 'Add some AmazingFeature'`
4. Branch'e push edin: `git push origin feature/AmazingFeature`
5. **Pull Request** açın

### Commit Kuralları
- `feat:` Yeni özellik
- `fix:` Hata düzeltme
- `docs:` Dokümantasyon
- `style:` Kod style
- `refactor:` Kod refactoring
- `test:` Test ekleme

---

## 📞 İletişim

- **Email**: info@K.Bulutspor.com
- **Website**: [K.Bulutspor.com](https://K.Bulutspor.com)
- **Instagram**: [@K.Bulutsporkulubu](https://instagram.com/K.Bulutsporkulubu)
- **Tel**: +90 XXX XXX XXXX

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

---

## ✍️ Yazarlar

- **Proje Sahibi**: K.Bulut Spor Kulübü
- **Geliştirici(ler)**: [Your Name/Team]
- **Son Güncelleme**: Mayıs 2026

---

## 🙏 İçerik Eksiklikleri

Aşağıdaki resimler eklenmeyi beklemektedir (Lütfen kendi resimlerinizi ekleyin):

1. **Banner/Hero Image** - Ana başlık altına
2. **Homepage Screenshot** - Web sitesinin ana sayfası
3. **Admin Dashboard Screenshot** - Yönetim panelinin görünümü
4. **Gallery Screenshot** - Galeri sayfasının örneği
5. **Mobile View Screenshot** - Mobil cihazda görünüm

### Resim Ekleme Adımları:
1. Resimleri projeye ekleyin (veya cloud storage kullanın)
2. README'de `<!-- ADD_YOUR_IMAGE_URL_HERE -->` yerlerine resim URL'lerini değiştirin
3. Örnekler:
```markdown
![Description](https://your-domain.com/image.png)
// veya yerel dosya:
![Description](./path/to/image.png)
```

---

**⭐ Eğer bu proje faydalı olduysa, lütfen star verin!**

**Made with ❤️ by K.Bulut Spor Kulübü**
=======
## Dosya Yapısı

```
website/
├── templates/          # HTML şablonları
├── static/            # CSS, JS, resimler
├── migrations/        # Veritabanı değişiklikleri
├── models.py          # Oyuncu, Maç, Haber
├── views.py           # İş mantığı
├── urls.py            # URL yönlendirmesi
├── admin.py           # Admin yapılandırması
└── apps.py            # App konfigürasyonu
```

## Admin Paneli

**URL:** `/admin`
**Kullanıcı:** admin
**Şifre:** (setup sırasında ayarlanan)

Oyuncuları, maçları ve haberleri yönet!

## Production Deployment

Tam deployment rehberi için bkz: [DEPLOYMENT.md](DEPLOYMENT.md)

### Desteklenen Platformlar
- Heroku
- AWS EC2
- DigitalOcean
- Azure
- Google Cloud
- Any VPS with Python 3.11+

## Özelleştirme

### Renkler Değiştirme
`website/static/css/style.css` dosyasında CSS değişkenlerini düzenle.

### Logo/Resim Ekleme
`website/static/img/` klasörüne dosyaları ekle.

### Sayfa İçeriği
Templates'deki Django template tags'ı güncelle veya admin panelinden yönet.

## Lisans

© 2026 Karabağlar Atletizim FK. Tüm hakları saklıdır.

## İletişim

- Email: info@karabaglarfk.com
- Telefon: +90 (555) 123-4567
- Web: [www.karabaglarfk.com](https://www.karabaglarfk.com)
=======
# KarabaglarSK-Website
>>>>>>> 967a45caea7f570dced7c65f737930f0a01cdff5
>>>>>>> 60e271c705f5d58f95bab4e10c1e29a1bde0bd73
