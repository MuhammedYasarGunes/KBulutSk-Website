# Karabağlar Atletik FK - Django Yapısı

Django web sitesini production-ready hale getirdim. İşte kurulum ve deployment yönergeleri:

## Proje Yapısı

```
KarabağlarAtletik/
├── karabaglar_project/          # Django proje konfigürasyonu
│   ├── __init__.py
│   ├── settings.py              # Proje ayarları
│   ├── urls.py                  # URL konfigürasyonu
│   ├── asgi.py                  # ASGI yapılandırması
│   └── wsgi.py                  # WSGI yapılandırması
├── website/                      # Django app
│   ├── migrations/              # Veritabanı migrasyonları
│   ├── static/                  # CSS, JS, resimler
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/               # HTML şablonları
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── galeri.html
│   │   ├── takim.html
│   │   ├── maclar.html
│   │   └── iletisim.html
│   ├── models.py                # Veritabanı modelleri
│   ├── views.py                 # View fonksiyonları
│   ├── urls.py                  # URL yönlendirmesi
│   ├── admin.py                 # Admin paneli yapılandırması
│   └── apps.py                  # App konfigürasyonu
├── manage.py                    # Django yönetim aracı
├── requirements.txt             # Python bağımlılıkları
├── .env.example                 # Ortam değişkenleri şablonu
├── Dockerfile                   # Docker yapılandırması
├── docker-compose.yml           # Docker Compose konfigürasyonu
├── Procfile                     # Heroku deployment
└── setup.sh                     # İlk kurulum betiği

## Yerel Kurulum

### 1. Sanal Ortam Oluştur
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# ya da
venv\Scripts\activate  # Windows
```

### 2. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 3. Ortam Değişkenlerini Ayarla
```bash
cp .env.example .env
# .env dosyasını düzenleyin gerekirse
```

### 4. Veritabanı Migrasyonları
```bash
python manage.py migrate
```

### 5. Admin Kullanıcı Oluştur
```bash
python manage.py createsuperuser
```

### 6. Static Dosyaları Topla
```bash
python manage.py collectstatic --noinput
```

### 7. Geliştirme Sunucusu Başlat
```bash
python manage.py runserver
```

Tarayıcıda açın: http://localhost:8000

## Docker ile Deployment

### Docker Compose Kullan (Önerilen)
```bash
docker-compose up -d
```

Erişim: http://localhost:8000

### Veya Manuel Docker
```bash
# İmaj inşa et
docker build -t karabaglar-atletik .

# Konteyner çalıştır
docker run -p 8000:8000 karabaglar-atletik
```

## Production Deployment

### Heroku'ya Deploy
```bash
# Heroku CLI'yi yükle
# Giriş yap
heroku login

# Heroku uygulaması oluştur
heroku create karabaglar-atletik

# Environment değişkenlerini ayarla
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy et
git push heroku main
```

### AWS/Azure/DigitalOcean
1. VPS sağlayıcısına sunucu oluştur (Ubuntu 22.04 önerilen)
2. `setup.sh` betiğini çalıştır
3. Nginx reverse proxy ayarla
4. SSL sertifikası kur (Let's Encrypt)
5. PM2 veya Supervisor ile Gunicorn yönet

## Admin Paneli

URL: http://localhost:8000/admin
Kullanıcı adı: admin
Şifre: (oluşturduğunuz şifre)

Admin panelinden yönetebileceğiniz:
- Oyuncular (Takım)
- Maçlar
- Haberler

## Önemli Ayarlar

### Production için `settings.py` Güncellemeleri
```python
# .env dosyasından yükle
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## Database Migrasyonu

SQLite'dan PostgreSQL'e geçiş:
```bash
# settings.py dosyasında DATABASE yapılandırmasını değiştir
# PostgreSQL kütüphanelerini yükle
pip install psycopg2-binary

# Migrasyonları çalıştır
python manage.py migrate
```

## Sorun Giderme

### Static dosyaları yüklenmiyorsa
```bash
python manage.py collectstatic --clear --noinput
```

### Veritabanı hataları
```bash
python manage.py flush  # Veritabanını sıfırla (DEĞİŞECEK!)
python manage.py migrate
```

### Admin paneli çalışmıyorsa
```bash
python manage.py createsuperuser
```

## İletişim Formu Ayarı

Email gönderme özelliğini aktifleştirmek için `.env` dosyasını güncelle:
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Güvenlik Kontrol Listesi

- [ ] SECRET_KEY'i değiştir
- [ ] DEBUG=False yap
- [ ] ALLOWED_HOSTS'u güncelle
- [ ] HTTPS'i etkinleştir
- [ ] Django güncellemelerini kontrol et
- [ ] Bağımlılıkları güncelle
- [ ] Düzenli backuplar al
- [ ] Log rotasyonunu ayarla

## Gelişmiş Ayarlar

### Email ile İletişim
1. Django-celery kurulumu
2. Background task işlemi
3. Email template'leri oluştur

### Caching
```bash
pip install django-redis
# settings.py'da Redis cache ayarla
```

### CDN Entegrasyonu
- AWS CloudFront
- Cloudflare
- MaxCDN

## Destek ve Sorular

Sorularınız olursa, lütfen admin panelinden iletişim formunu kullanın.

---
**Sürüm:** 1.0.0
**Son Güncelleme:** Nisan 2026
**Django Versiyonu:** 5.0.3
