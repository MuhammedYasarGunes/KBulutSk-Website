from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from website.models import Haber, Takim

YONETIM_SAYFALARI = ["index", "haberler", "oyuncular", "takimlar", "maclar", "galeri"]


class YetkiTestleri(TestCase):
    def test_giris_yapmayan_kullanici_login_sayfasina_yonlenir(self):
        for ad in YONETIM_SAYFALARI:
            with self.subTest(sayfa=ad):
                url = reverse(f"dashboard:{ad}")
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertIn(reverse("dashboard:login"), response["Location"])

    def test_login_sayfasi_acilir(self):
        response = self.client.get(reverse("dashboard:login"))
        self.assertEqual(response.status_code, 200)


class YonetimPaneliTestleri(TestCase):
    def setUp(self):
        self.kullanici = get_user_model().objects.create_user("yonetici", password="gizli-Sifre-123")
        self.client.force_login(self.kullanici)

    def test_giris_yapan_kullanici_tum_listeleri_gorur(self):
        for ad in YONETIM_SAYFALARI:
            with self.subTest(sayfa=ad):
                self.assertEqual(self.client.get(reverse(f"dashboard:{ad}")).status_code, 200)

    def test_ozet_sayilari_dogrudur(self):
        Takim.objects.create(ad="A Takımı")
        Haber.objects.create(başlık="Duyuru", içerik="metin")
        response = self.client.get(reverse("dashboard:index"))
        self.assertEqual(response.context["toplam_takim"], 1)
        self.assertEqual(response.context["toplam_haber"], 1)

    def test_formdan_takim_eklenir(self):
        response = self.client.post(reverse("dashboard:takim_ekle"), {"ad": "U10 Takımı"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Takim.objects.filter(ad="U10 Takımı").exists())
