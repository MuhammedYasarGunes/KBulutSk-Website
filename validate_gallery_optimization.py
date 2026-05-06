#!/usr/bin/env python3
"""
Galeri Optimizasyon Doğrulama Scripti
Tüm optimizasyonların düzgün uygulanmış olup olmadığını kontrol eder.
"""

import os
import re
from pathlib import Path

class GalleryOptimizationValidator:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.issues = []
        self.warnings = []
        self.successes = []
        
    def check_css_optimizations(self):
        """CSS optimizasyonlarını kontrol et"""
        css_file = self.project_root / 'website' / 'static' / 'css' / 'style.css'
        
        if not css_file.exists():
            self.issues.append(f"❌ CSS dosyası bulunamadı: {css_file}")
            return
            
        content = css_file.read_text()
        
        # Backdrop filter @supports check
        if '@supports (backdrop-filter: blur(10px))' in content:
            self.successes.append("✅ Backdrop filter @supports directive var")
        else:
            self.issues.append("❌ Backdrop filter @supports directive eksik")
            
        # Shimmer animation check
        if '@keyframes shimmer' in content:
            self.successes.append("✅ Shimmer animation tanımı var")
        else:
            self.issues.append("❌ Shimmer animation eksik")
            
        # Prefers-reduced-motion check
        if '@media (prefers-reduced-motion: reduce)' in content:
            self.successes.append("✅ prefers-reduced-motion support var")
        else:
            self.warnings.append("⚠️  prefers-reduced-motion support eksik")
            
        # Loading class check
        if '.gallery-image.loading' in content:
            self.successes.append("✅ Loading class styles var")
        else:
            self.issues.append("❌ Loading class styles eksik")
            
        # Will-change check
        if 'will-change: opacity' in content:
            self.successes.append("✅ Will-change optimization var")
        else:
            self.warnings.append("⚠️  Will-change optimization eksik")
    
    def check_lazy_loading_js(self):
        """Lazy loading JavaScript dosyasını kontrol et"""
        js_file = self.project_root / 'website' / 'static' / 'js' / 'lazy-loading.js'
        
        if not js_file.exists():
            self.issues.append(f"❌ Lazy-loading.js bulunamadı: {js_file}")
            return
            
        content = js_file.read_text()
        
        # IntersectionObserver check
        if 'IntersectionObserver' in content:
            self.successes.append("✅ IntersectionObserver kullanılıyor")
        else:
            self.issues.append("❌ IntersectionObserver implementasyonu eksik")
            
        # Debounce check
        if 'function debounce' in content:
            self.successes.append("✅ Debounce utility var")
        else:
            self.issues.append("❌ Debounce utility eksik")
            
        # RequestAnimationFrame check
        if 'requestAnimationFrame' in content:
            self.successes.append("✅ requestAnimationFrame kullanılıyor")
        else:
            self.issues.append("❌ requestAnimationFrame kulllanılmıyor")
            
        # GalleryLazyLoader class check
        if 'class GalleryLazyLoader' in content:
            self.successes.append("✅ GalleryLazyLoader sınıfı var")
        else:
            self.issues.append("❌ GalleryLazyLoader sınıfı eksik")
            
        # File size check
        file_size = js_file.stat().st_size / 1024  # KB
        if file_size < 15:  # 15 KB altında olmalı
            self.successes.append(f"✅ Lazy-loading.js boyutu optimal ({file_size:.1f} KB)")
        else:
            self.warnings.append(f"⚠️  Lazy-loading.js çok büyük ({file_size:.1f} KB)")
    
    def check_gallery_html(self):
        """Galeri HTML template'ini kontrol et"""
        html_file = self.project_root / 'website' / 'templates' / 'galeri.html'
        
        if not html_file.exists():
            self.issues.append(f"❌ Galeri template bulunamadı: {html_file}")
            return
            
        content = html_file.read_text()
        
        # Lazy class check
        if 'class="gallery-item lazy"' in content:
            self.successes.append("✅ Gallery items lazy class'ı var")
        else:
            self.issues.append("❌ Gallery items lazy class'ı eksik")
            
        # Data-src attribute check
        if 'data-src=' in content:
            self.successes.append("✅ Resimler data-src attribute'ü kullanıyor")
        else:
            self.issues.append("❌ Resimler data-src attribute'ünü kullanmıyor")
            
        # SVG placeholder check
        if 'data:image/svg+xml' in content:
            self.successes.append("✅ SVG placeholder kullanılıyor")
        else:
            self.warnings.append("⚠️  SVG placeholder kullanılmıyor")
            
        # Lazy-loading.js script check
        if 'lazy-loading.js' in content:
            self.successes.append("✅ Lazy-loading.js script tag'i var")
        else:
            self.issues.append("❌ Lazy-loading.js script tag'i eksik")
            
        # Video preload check
        if 'preload="none"' in content or 'preload="metadata"' in content:
            self.successes.append("✅ Video preload attribute'leri optimize edilmiş")
        else:
            self.warnings.append("⚠️  Video preload attribute'leri kontrol et")
            
        # Data-bg-image check
        if 'data-bg-image=' in content:
            self.successes.append("✅ YouTube thumbnail'lar lazy load'a hazır")
        else:
            self.warnings.append("⚠️  YouTube thumbnail'lar lazy load'a alınmalı")
    
    def check_script_js(self):
        """Ana script.js dosyasını kontrol et"""
        js_file = self.project_root / 'website' / 'static' / 'js' / 'script.js'
        
        if not js_file.exists():
            self.issues.append(f"❌ Script.js bulunamadı: {js_file}")
            return
            
        content = js_file.read_text()
        
        # Eski gallery filter kodu kontrol et
        if 'const filterButtons = document.querySelectorAll(\'.filter-btn\');' in content:
            # Sadece başlatma kısmı olup olmadığını kontrol et
            filter_count = content.count('document.querySelectorAll(\'.filter-btn\')')
            if filter_count > 1:
                self.issues.append("❌ Eski gallery filter kodu script.js'de hala var")
            else:
                self.successes.append("✅ Eski gallery filter kodu kaldırıldı")
        else:
            self.successes.append("✅ Eski gallery filter kodu kaldırıldı")
    
    def check_documentation(self):
        """Dokümantasyon dosyalarını kontrol et"""
        docs = [
            self.project_root / 'GALERI_OPTIMIZASYONU.md',
            self.project_root / 'GALERI_HIZLI_BASLANGIC.md'
        ]
        
        for doc in docs:
            if doc.exists():
                self.successes.append(f"✅ Dokümantasyon var: {doc.name}")
            else:
                self.warnings.append(f"⚠️  Dokümantasyon eksik: {doc.name}")
    
    def run_all_checks(self):
        """Tüm kontrolleri çalıştır"""
        print("🔍 Galeri Optimizasyon Doğrulama Başlıyor...\n")
        
        self.check_css_optimizations()
        self.check_lazy_loading_js()
        self.check_gallery_html()
        self.check_script_js()
        self.check_documentation()
        
        self.print_results()
    
    def print_results(self):
        """Sonuçları yazdır"""
        print("\n" + "="*60)
        print("📊 SONUÇLAR")
        print("="*60 + "\n")
        
        if self.successes:
            print("✅ BAŞARILI KONTROLLER:")
            for success in self.successes:
                print(f"  {success}")
            print()
        
        if self.warnings:
            print("⚠️  UYARILAR:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if self.issues:
            print("❌ HATALAR:")
            for issue in self.issues:
                print(f"  {issue}")
            print()
        
        print("="*60)
        
        # Sonuç özeti
        total = len(self.successes) + len(self.warnings) + len(self.issues)
        success_rate = (len(self.successes) / total * 100) if total > 0 else 0
        
        print(f"\n📈 Başarı Oranı: {success_rate:.1f}%")
        print(f"   ✅ {len(self.successes)} başarılı")
        print(f"   ⚠️  {len(self.warnings)} uyarı")
        print(f"   ❌ {len(self.issues)} hata")
        
        if self.issues:
            print("\n🔧 HATA GİDERME:")
            print("  Yukarıdaki hataları düzeltmek için GALERI_OPTIMIZASYONU.md")
            print("  dosyasını kontrol edin.")
        else:
            print("\n🎉 Tüm optimizasyonlar başarıyla uygulanmış!")
        
        print("="*60 + "\n")


if __name__ == '__main__':
    import sys
    
    # Proje kök dizinini bul
    project_root = Path(__file__).parent
    
    validator = GalleryOptimizationValidator(project_root)
    validator.run_all_checks()
    
    # Exit code: hata varsa 1, yoksa 0
    sys.exit(1 if validator.issues else 0)
