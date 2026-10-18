import re
from datetime import timedelta
from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import GaleriÖğesi, Haber, Mac, Oyuncu, Takim


class SayfaYuklemeTestleri(TestCase):
    """Herkese açık sayfalar boş veritabanında da açılmalı."""

    def test_herkese_acik_sayfalar_200_doner(self):
        for ad in ["index", "galeri", "takim", "maclar", "iletisim", "kulup_yonetimi"]:
            with self.subTest(sayfa=ad):
                response = self.client.get(reverse(f"website:{ad}"))
                self.assertEqual(response.status_code, 200)

    def test_ana_sayfa_en_fazla_bes_haber_gosterir(self):
        for i in range(7):
            Haber.objects.create(başlık=f"Haber {i}", içerik="içerik")
        response = self.client.get(reverse("website:index"))
        self.assertEqual(len(response.context["haberler"]), 5)

    def test_iletisim_formu_gonderilince_onay_gosterir(self):
        response = self.client.post(
            reverse("website:iletisim"),
            {"ad": "Ali", "email": "ali@example.com", "konu": "Kayıt", "mesaj": "Merhaba"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["mesaj_gönderildi"])


class MacIstatistikTestleri(TestCase):
    def setUp(self):
        self.takim = Takim.objects.create(ad="K.Bulut U14")
        simdi = timezone.now()
        sonuclar = ["kazanildi", "kazanildi", "berabere", "kaybedildi", "gelecek"]
        for gun, durum in enumerate(sonuclar):
            Mac.objects.create(
                takim=self.takim, ev_sahibi="K.Bulut", misafir=f"Rakip {gun}",
                tarih=simdi - timedelta(days=gun), lig="U14 Ligi", durum=durum,
            )

    def test_galibiyet_beraberlik_maglubiyet_dogru_sayilir(self):
        response = self.client.get(reverse("website:maclar"))
        self.assertEqual(response.context["toplam_maç"], 4)
        self.assertEqual(response.context["kazanılan"], 2)
        self.assertEqual(response.context["berabere"], 1)
        self.assertEqual(response.context["kaybedilen"], 1)
        self.assertEqual(response.context["gelecek_maçlar"].count(), 1)


class TakimApiTestleri(TestCase):
    def test_takimin_oyunculari_json_doner(self):
        takim = Takim.objects.create(ad="K.Bulut U16")
        Oyuncu.objects.create(takim=takim, ad="Can", pozisyon="Forvet", numara=9)
        Oyuncu.objects.create(takim=takim, ad="Ege", pozisyon="Kaleci", numara=1)
        response = self.client.get(reverse("website:takim_oyuncular_api", args=[takim.id]))
        self.assertEqual(response.status_code, 200)
        veri = response.json()
        self.assertEqual(veri["takim"], "K.Bulut U16")
        self.assertEqual({o["numara"] for o in veri["oyuncular"]}, {1, 9})

    def test_olmayan_takim_404_doner(self):
        response = self.client.get(reverse("website:takim_oyuncular_api", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_api_yalnizca_get_kabul_eder(self):
        takim = Takim.objects.create(ad="K.Bulut U12")
        response = self.client.post(reverse("website:takim_oyuncular_api", args=[takim.id]))
        self.assertEqual(response.status_code, 405)


class GaleriYoutubeTestleri(TestCase):
    def oge(self, url):
        return GaleriÖğesi(başlık="Video", video_url=url)

    def test_tum_youtube_link_bicimlerinden_kimlik_cikar(self):
        kimlik = "dQw4w9WgXcQ"
        linkler = [
            f"https://www.youtube.com/watch?v={kimlik}",
            f"https://youtu.be/{kimlik}",
            f"https://www.youtube.com/embed/{kimlik}",
            f"https://www.youtube.com/shorts/{kimlik}",
            f"https://www.youtube.com/live/{kimlik}",
            f"https://www.youtube.com/watch?feature=share&v={kimlik}",
            kimlik,
        ]
        for link in linkler:
            with self.subTest(link=link):
                self.assertEqual(self.oge(link).get_youtube_id, kimlik)

    def test_youtube_olmayan_link_kimlik_vermez(self):
        oge = self.oge("https://vimeo.com/123456")
        self.assertIsNone(oge.get_youtube_id)
        self.assertFalse(oge.has_youtube_video)
        self.assertTrue(oge.is_video)

    def test_linksiz_oge_video_sayilmaz(self):
        oge = GaleriÖğesi(başlık="Fotoğraf")
        self.assertFalse(oge.is_video)
        self.assertFalse(oge.has_youtube_video)
        self.assertIsNone(oge.get_youtube_id)


class ModelMetinTestleri(TestCase):
    def test_str_metotlari_okunabilir_metin_doner(self):
        takim = Takim.objects.create(ad="K.Bulut U18")
        oyuncu = Oyuncu.objects.create(takim=takim, ad="Deniz", pozisyon="Defans", numara=4)
        mac = Mac.objects.create(
            takim=takim, ev_sahibi="K.Bulut", misafir="Bornova",
            tarih=timezone.now(), lig="U18 Ligi",
        )
        self.assertEqual(str(takim), "K.Bulut U18")
        self.assertEqual(str(oyuncu), "Deniz - #4")
        self.assertEqual(str(mac), "K.Bulut vs Bornova")
        self.assertEqual(str(GaleriÖğesi.objects.create()), f"Galeri Öğesi #{GaleriÖğesi.objects.first().id}")


class StatikDosyaTestleri(TestCase):
    """Şablonlardaki her {% static %} yolu gerçekten var olmalı.

    Canlıda (DEBUG=False, ManifestStaticFilesStorage) olmayan bir dosyaya verilen
    static etiketi sayfayı 500 hatasıyla düşürür; HTML yorumu içinde olsa bile.
    """

    def test_sablonlardaki_statik_yollar_mevcut(self):
        etiket = re.compile(r"""{%\s*static\s+['"]([^'"]+)['"]\s*%}""")
        sablonlar = list(Path(settings.BASE_DIR).glob("*/templates/**/*.html"))
        self.assertTrue(sablonlar)
        eksikler = [
            f"{sablon.relative_to(settings.BASE_DIR)}: {yol}"
            for sablon in sablonlar
            for yol in etiket.findall(sablon.read_text(encoding="utf-8"))
            if finders.find(yol) is None
        ]
        self.assertEqual(eksikler, [])
