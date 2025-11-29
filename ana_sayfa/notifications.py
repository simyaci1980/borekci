from django.core.mail import send_mail
from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)


def send_email_notification(siparis):
    """Yeni sipariş geldiğinde e-posta gönder"""
    musteri_bilgi = siparis.ad_soyad if siparis.ad_soyad else siparis.telefon
    subject = f'🥟 Yeni Sipariş - {musteri_bilgi}'
    
    message = f"""
    YENİ SİPARİŞ GELDİ!
    
    📞 Telefon: {siparis.telefon}
    
    🥟 Ürün: {siparis.borek.ad}
    📦 Adet: {siparis.adet}
    💰 Toplam: {siparis.toplam_fiyat} TL
    
    📍 Adres:
    {siparis.adres}
    
    📝 Not: {siparis.not_mesaj or 'Not yok'}
    
    ⏰ Sipariş Zamanı: {siparis.siparis_tarihi.strftime('%d/%m/%Y %H:%M')}
    
    ---
    Admin panelinden kontrol edin: http://127.0.0.1:8000/admin/
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"E-posta gönderilemedi: {e}")
        return False


def send_telegram_notification(siparis):
    """Yeni sipariş geldiğinde Telegram'a mesaj gönder"""
    
    if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
        return False
    
    message = f"""
🥟 *YENİ SİPARİŞ GELDİ!*

📞 Telefon:
`{siparis.telefon}`

🥟 Ürün: {siparis.borek.ad}
📦 Adet: {siparis.adet}
💰 Toplam: {siparis.toplam_fiyat} TL

📍 Adres:
`{siparis.adres}`

📝 Not: {siparis.not_mesaj or 'Yok'}

⏰ {siparis.siparis_tarihi.strftime('%d/%m/%Y %H:%M')}
"""
    
    try:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=data, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Telegram mesajı gönderilemedi: {e}")
        return False


def send_order_notifications(siparis):
    """Hem e-posta hem Telegram bildirimi gönder"""
    email_sent = send_email_notification(siparis)
    telegram_sent = send_telegram_notification(siparis)
    
    return {
        'email': email_sent,
        'telegram': telegram_sent
    }


def send_status_notification(siparis):
    """
    Sipariş durumu değiştiğinde müşteriye bildirim gönderir
    """
    durum_mesajlari = {
        'yeni': '🆕 Siparişiniz alındı! En kısa sürede hazırlamaya başlayacağız.',
        'hazirlaniyor': '👨‍🍳 Siparişiniz hazırlanıyor! Taze börekleriniz fırından çıkıyor.',
        'yolda': '🚗 Siparişiniz yola çıktı! Yakında kapınızda olacak.',
        'teslim_edildi': '✅ Siparişiniz teslim edildi! Afiyet olsun! 😊',
        'iptal': '❌ Siparişiniz iptal edildi. Bilgi için: 0507 017 52 43',
    }
    
    durum_metni = siparis.get_durum_display()
    bildirim_mesaji = durum_mesajlari.get(siparis.durum, '')
    
    # Email bildirimi
    email_subject = f"Sipariş Durumu: {durum_metni}"
    email_body = f"""
    Merhaba,
    
    {bildirim_mesaji}
    
    Sipariş Detayları:
    -----------------
    Ürün: {siparis.borek.ad}
    Adet: {siparis.adet} adet
    Toplam Tutar: {siparis.toplam_fiyat} TL
    Durum: {durum_metni}
    
    Teslimat Adresi: {siparis.adres}
    
    Sorularınız için: 0507 017 52 43
    WhatsApp: https://wa.me/905070175243
    
    Teşekkürler,
    Börekçi Teyzeler
    """
    
    success = True
    
    # Email gönder (eğer email varsa)
    if siparis.email:
        try:
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[siparis.email],
                fail_silently=False,
            )
            logger.info(f"Durum değişikliği email bildirimi gönderildi: {siparis.email}")
        except Exception as e:
            logger.error(f"Email gönderilemedi: {str(e)}")
            success = False
    
    # Telegram bildirimi (size)
    try:
        telegram_mesaji = f"""
🔔 *SİPARİŞ DURUMU GÜNCELLENDİ*

{bildirim_mesaji}

📦 *Detaylar:*
Ürün: {siparis.borek.ad}
Adet: {siparis.adet}
Tutar: {siparis.toplam_fiyat} TL
*Durum: {durum_metni}*

📞 Telefon: `{siparis.telefon}`
📍 Adres: {siparis.adres[:50]}...
        """.strip()
        
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': telegram_mesaji,
            'parse_mode': 'Markdown'
        }
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            logger.info(f"Durum değişikliği Telegram bildirimi gönderildi")
        else:
            logger.error(f"Telegram hatası: {response.text}")
            success = False
            
    except Exception as e:
        logger.error(f"Telegram bildirimi gönderilemedi: {str(e)}")
        success = False
    
    return success
