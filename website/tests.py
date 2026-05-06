from django.test import TestCase


# Create your tests here.
class WebsiteViewsTestCase(TestCase):
    """Website views test case"""
    
    def test_index_page_loads(self):
        """Ana sayfa yüklenme testi"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_galeri_page_loads(self):
        """Galeri sayfası yüklenme testi"""
        response = self.client.get('/galeri/')
        self.assertEqual(response.status_code, 200)
    
    def test_takim_page_loads(self):
        """Takım sayfası yüklenme testi"""
        response = self.client.get('/takim/')
        self.assertEqual(response.status_code, 200)
    
    def test_maclar_page_loads(self):
        """Maçlar sayfası yüklenme testi"""
        response = self.client.get('/maclar/')
        self.assertEqual(response.status_code, 200)
    
    def test_iletisim_page_loads(self):
        """İletişim sayfası yüklenme testi"""
        response = self.client.get('/iletisim/')
        self.assertEqual(response.status_code, 200)
