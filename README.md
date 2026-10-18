# K. Bulut Spor Kulübü · Web Sitesi

[![tests](https://github.com/MuhammedYasarGunes/KBulutSk-Website/actions/workflows/tests.yml/badge.svg)](https://github.com/MuhammedYasarGunes/KBulutSk-Website/actions/workflows/tests.yml)
![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Django 5.0](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-Apache--2.0-blue)

İzmir Konak'taki K. Bulut Spor Kulübü için geliştirilen web sitesi: takım, maç, galeri ve iletişim sayfaları ile kulüp yönetiminin kendi içeriğini girdiği özel bir yönetim paneli.

> **English:** Website for an amateur sports club in İzmir, Türkiye. Django + PostgreSQL, Cloudinary for media, Docker Compose for deployment. Includes a custom admin dashboard for club staff, a small JSON API and a pytest suite that runs on GitHub Actions.

<p align="center">
  <img src="docs/maclar-sayfasi.jpg" width="760" alt="Maçlar sayfası (örnek verilerle yerelde çalıştırıldı)">
  <br><sub>Maçlar sayfası, örnek verilerle yerelde çalıştırıldı.</sub>
</p>

## Özellikler

- **Kulüp sayfaları:** ana sayfa, takım, maçlar, galeri, iletişim ve kulüp yönetimi
- **Yönetim paneli** (`/dashboard/`): haber, oyuncu, takım, maç, galeri ve yönetim kurulu kayıtlarını ekleme, düzenleme ve silme; giriş zorunlu
- **Galeri:** Cloudinary üzerinde fotoğraf ve video; her biçimdeki YouTube linkinden (watch, youtu.be, embed, shorts, live) video kimliği çıkarma
- **Maç sonuçları:** kazanılan, berabere biten, kaybedilen ve gelecek maçlar ayrı renklerle; istatistikler sonuçlardan hesaplanır
- **JSON API:** `GET /api/takim/<id>/oyuncular/` takımın oyuncularını döndürür

## Teknolojiler

| Katman | Teknoloji |
|---|---|
| Backend | Python 3.11, Django 5.0 |
| Veritabanı | PostgreSQL 15 (testlerde SQLite) |
| Medya / statik | Cloudinary, WhiteNoise |
| Sunucu | Gunicorn, Docker Compose |
| Test / CI | pytest, pytest-django, GitHub Actions |

## Proje yapısı

```
karabaglar_project/   ayarlar (settings.py, test için settings_test.py), URL'ler
website/              herkese açık sayfalar, modeller, şablonlar, statik dosyalar, JSON API
dashboard/            giriş zorunlu yönetim paneli ve formlar
.github/workflows/    her push ve PR'da testler
```

> Proje paketinin adı (`karabaglar_project`), sitenin aynı altyapıyla geliştirilen Karabağlar Atletik SK sitesinden gelir; yayındaki kurulumları bozmamak için değiştirilmedi.

## Yerelde çalıştırma

Docker ile:

```bash
git clone https://github.com/MuhammedYasarGunes/KBulutSk-Website.git
cd KBulutSk-Website
cp .env.example .env          # değerleri doldur
docker compose up --build     # http://localhost:8000
```

Docker olmadan (SQLite ile):

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
export DEBUG=True SECRET_KEY=dev DATABASE_URL=sqlite:///db.sqlite3 CLOUDINARY_URL=cloudinary://key:secret@name
python manage.py migrate
python manage.py createsuperuser   # panel girişi için
python manage.py runserver
```

## Testler

```bash
pytest
```

19 test şunları kapsar:

- tüm sayfaların açılması
- maç istatistikleri ve maç durumlarının doğru görünmesi
- JSON API (200 / 404 / 405)
- YouTube link ayrıştırma
- panelin giriş zorunluluğu ve formdan kayıt ekleme
- şablonlardaki her `{% static %}` yolunun gerçekten var olması

GitHub Actions her push ve pull request'te `manage.py check`, eksik migration kontrolü ve testleri çalıştırır.

## Yayına alma

Docker Compose (web + PostgreSQL) ile, önde HTTPS sağlayan bir ters vekil sunucuyla (ör. Nginx). Tüm gizli değerler `.env` dosyasından okunur; şablon için [`.env.example`](.env.example) dosyasına bakın. Veritabanı portu yalnızca sunucunun kendisine (127.0.0.1) açıktır. `setup.sh`, `DJANGO_SUPERUSER_*` değişkenleri verilirse ilk yönetici hesabını oluşturur.

## Lisans

[Apache-2.0](LICENSE) · Geliştiren: [Muhammed Yaşar Güneş](https://github.com/MuhammedYasarGunes)
