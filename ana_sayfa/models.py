from django.db import models
from django.utils import timezone


class BorekCesidi(models.Model):
    """Börek çeşitleri"""
    ad = models.CharField(max_length=100, verbose_name="Börek Adı")
    aciklama = models.TextField(verbose_name="Açıklama")
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat (TL)")
    resim = models.ImageField(upload_to='borekler/', null=True, blank=True, verbose_name="Ürün Resmi")
    aktif = models.BooleanField(default=True, verbose_name="Aktif")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Börek Çeşidi"
        verbose_name_plural = "Börek Çeşitleri"
        ordering = ['ad']
    
    def __str__(self):
        return f"{self.ad} - {self.fiyat} TL"


class Siparis(models.Model):
    """Müşteri siparişleri"""
    DURUM_SECENEKLERI = [
        ('yeni', 'Yeni Sipariş'),
        ('hazirlaniyor', 'Hazırlanıyor'),
        ('yolda', 'Yolda'),
        ('teslim_edildi', 'Teslim Edildi'),
        ('iptal', 'İptal Edildi'),
    ]
    
    ad_soyad = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ad Soyad")
    telefon = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(blank=True, null=True, verbose_name="E-posta")
    adres = models.TextField(verbose_name="Teslimat Adresi")
    borek = models.ForeignKey(BorekCesidi, on_delete=models.CASCADE, verbose_name="Börek Çeşidi")
    adet = models.PositiveIntegerField(default=1, verbose_name="Adet")
    not_mesaj = models.TextField(blank=True, null=True, verbose_name="Sipariş Notu")
    durum = models.CharField(max_length=20, choices=DURUM_SECENEKLERI, default='yeni', verbose_name="Sipariş Durumu")
    toplam_fiyat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Toplam Fiyat")
    siparis_tarihi = models.DateTimeField(default=timezone.now, verbose_name="Sipariş Tarihi")
    
    class Meta:
        verbose_name = "Sipariş"
        verbose_name_plural = "Siparişler"
        ordering = ['-siparis_tarihi']
    
    def __str__(self):
        isim = self.ad_soyad if self.ad_soyad else self.telefon
        return f"{isim} - {self.borek.ad} ({self.adet} adet)"
    
    def save(self, *args, **kwargs):
        # Toplam fiyatı otomatik hesapla
        self.toplam_fiyat = self.borek.fiyat * self.adet
        super().save(*args, **kwargs)


class Iletisim(models.Model):
    """İletişim formu mesajları"""
    ad_soyad = models.CharField(max_length=200, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    telefon = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    mesaj = models.TextField(verbose_name="Mesaj")
    okundu = models.BooleanField(default=False, verbose_name="Okundu")
    tarih = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")
    
    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-tarih']
    
    def __str__(self):
        return f"{self.ad_soyad} - {self.tarih.strftime('%d/%m/%Y %H:%M')}"
