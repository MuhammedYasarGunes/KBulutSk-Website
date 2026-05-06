<<<<<<< HEAD
# Karabağlar Atletik FK - Django Web Sitesi

Karabağlar Atletik FK'nin tam özellikli Django web sitesi uygulaması.

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
```bash
docker-compose up -d
```

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
