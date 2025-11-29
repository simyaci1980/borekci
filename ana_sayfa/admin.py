from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import BorekCesidi, Siparis, Iletisim
import urllib.parse


@admin.register(BorekCesidi)
class BorekCesidiAdmin(admin.ModelAdmin):
    list_display = ['ad', 'fiyat', 'aktif', 'olusturulma_tarihi']
    list_filter = ['aktif', 'olusturulma_tarihi']
    search_fields = ['ad', 'aciklama']
    list_editable = ['aktif']


@admin.register(Siparis)
class SiparisAdmin(admin.ModelAdmin):
    list_display = ['telefon', 'borek', 'adet', 'toplam_fiyat', 'durum', 'siparis_tarihi', 'whatsapp_button']
    list_filter = ['durum', 'siparis_tarihi', 'borek']
    search_fields = ['telefon', 'adres', 'ad_soyad']
    list_editable = ['durum']
    readonly_fields = ['toplam_fiyat', 'siparis_tarihi', 'whatsapp_link']
    date_hierarchy = 'siparis_tarihi'
    
    def whatsapp_button(self, obj):
        """Sipariş listesinde WhatsApp butonu"""
        durum_mesajlari = {
            'yeni': '🆕 Siparişiniz alındı! En kısa sürede hazırlamaya başlayacağız.',
            'hazirlaniyor': '👨‍🍳 Siparişiniz hazırlanıyor! Taze börekleriniz fırından çıkıyor.',
            'yolda': '🚗 Siparişiniz yola çıktı! Yakında kapınızda olacak.',
            'teslim_edildi': '✅ Siparişiniz teslim edildi! Afiyet olsun! 😊',
            'iptal': '❌ Siparişiniz iptal edildi.',
        }
        
        durum_metni = obj.get_durum_display()
        mesaj = durum_mesajlari.get(obj.durum, '')
        
        whatsapp_mesaji = f"""{mesaj}

📦 Sipariş: {obj.borek.ad}
📊 Adet: {obj.adet}
💰 Tutar: {obj.toplam_fiyat} TL
📍 Durum: {durum_metni}

Teşekkürler,
Börekçi Teyzeler 🥟"""
        
        telefon = obj.telefon.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        if telefon.startswith('0'):
            telefon = '90' + telefon[1:]
        
        encoded_message = urllib.parse.quote(whatsapp_mesaji)
        whatsapp_url = f"https://wa.me/{telefon}?text={encoded_message}"
        
        return format_html(
            '<a href="{}" target="_blank" style="background-color: #25D366; color: white; padding: 5px 10px; text-decoration: none; border-radius: 5px; display: inline-block;">'
            '📱 WhatsApp'
            '</a>',
            whatsapp_url
        )
    whatsapp_button.short_description = 'Bildirim Gönder'
    
    def whatsapp_link(self, obj):
        """Sipariş detayında WhatsApp linki"""
        durum_mesajlari = {
            'yeni': '🆕 Siparişiniz alındı! En kısa sürede hazırlamaya başlayacağız.',
            'hazirlaniyor': '👨‍🍳 Siparişiniz hazırlanıyor! Taze börekleriniz fırından çıkıyor.',
            'yolda': '🚗 Siparişiniz yola çıktı! Yakında kapınızda olacak.',
            'teslim_edildi': '✅ Siparişiniz teslim edildi! Afiyet olsun! 😊',
            'iptal': '❌ Siparişiniz iptal edildi.',
        }
        
        durum_metni = obj.get_durum_display()
        mesaj = durum_mesajlari.get(obj.durum, '')
        
        whatsapp_mesaji = f"""{mesaj}

📦 Sipariş: {obj.borek.ad}
📊 Adet: {obj.adet}
💰 Tutar: {obj.toplam_fiyat} TL
📍 Durum: {durum_metni}

Teşekkürler,
Börekçi Teyzeler 🥟"""
        
        telefon = obj.telefon.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        if telefon.startswith('0'):
            telefon = '90' + telefon[1:]
        
        encoded_message = urllib.parse.quote(whatsapp_mesaji)
        whatsapp_url = f"https://wa.me/{telefon}?text={encoded_message}"
        
        return format_html(
            '<a href="{}" target="_blank" style="background-color: #25D366; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; font-size: 16px;">'
            '📱 Müşteriye WhatsApp ile Durum Bildirimi Gönder'
            '</a>',
            whatsapp_url
        )
    whatsapp_link.short_description = 'WhatsApp Bildirimi'
    
    fieldsets = (
        ('Müşteri Bilgileri', {
            'fields': ('ad_soyad', 'telefon', 'email', 'adres')
        }),
        ('Sipariş Detayları', {
            'fields': ('borek', 'adet', 'toplam_fiyat', 'not_mesaj')
        }),
        ('Durum ve Tarih', {
            'fields': ('durum', 'siparis_tarihi')
        }),
        ('WhatsApp Bildirimi', {
            'fields': ('whatsapp_link',),
            'description': 'Durum değişikliğini müşteriye bildirmek için WhatsApp butonuna tıklayın.'
        }),
    )


@admin.register(Iletisim)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ['ad_soyad', 'email', 'telefon', 'okundu', 'tarih']
    list_filter = ['okundu', 'tarih']
    search_fields = ['ad_soyad', 'email', 'mesaj']
    list_editable = ['okundu']
    readonly_fields = ['tarih']
    date_hierarchy = 'tarih'
