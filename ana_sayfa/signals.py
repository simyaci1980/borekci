from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Siparis
from .notifications import send_status_notification
import logging

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Siparis)
def track_status_change(sender, instance, **kwargs):
    """
    Sipariş durumu değişikliğini takip et
    """
    if instance.pk:  # Eğer sipariş zaten varsa (güncelleme)
        try:
            old_instance = Siparis.objects.get(pk=instance.pk)
            instance._old_durum = old_instance.durum
        except Siparis.DoesNotExist:
            instance._old_durum = None
    else:  # Yeni sipariş
        instance._old_durum = None


@receiver(post_save, sender=Siparis)
def notify_status_change(sender, instance, created, **kwargs):
    """
    Sipariş durumu değiştiğinde müşteriye bildirim gönder
    Not: Bu fonksiyon devre dışı - Durum bildirimi admin panelden WhatsApp butonu ile manuel gönderilecek
    """
    # Otomatik bildirim kapatıldı - Admin panelden manuel WhatsApp gönderimi tercih edildi
    pass
