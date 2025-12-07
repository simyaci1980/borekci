from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BorekCesidi, Siparis, Iletisim
from .forms import SiparisForm, IletisimForm
from .notifications import send_order_notifications
from datetime import datetime
import pytz


def ana_sayfa(request):
    """Ana sayfa - Tek sayfalık börek satış sitesi"""
    borekler = BorekCesidi.objects.filter(aktif=True)
    siparis_form = SiparisForm()
    
    # Börek seçimi için boş seçenek ekle
    siparis_form.fields['borek'].empty_label = "🥟 Lezzet seçiniz..."
    
    iletisim_form = IletisimForm()
    
    # Çalışma saati kontrolü (08:00 - 23:00)
    istanbul_tz = pytz.timezone('Europe/Istanbul')
    now = datetime.now(istanbul_tz)
    current_hour = now.hour
    
    # Sipariş saatleri: 08:00 - 23:00 arası
    is_open = 8 <= current_hour < 23
    
    context = {
        'borekler': borekler,
        'siparis_form': siparis_form,
        'iletisim_form': iletisim_form,
        'is_open': is_open,
        'current_time': now.strftime('%H:%M'),
    }
    return render(request, 'ana_sayfa/index.html', context)


def siparis_olustur(request):
    """Sipariş oluşturma"""
    if request.method == 'POST':
        # Çalışma saati kontrolü
        istanbul_tz = pytz.timezone('Europe/Istanbul')
        now = datetime.now(istanbul_tz)
        current_hour = now.hour
        
        if not (8 <= current_hour < 23):
            messages.error(request, '⏰ Sipariş saatlerimiz 08:00 - 23:00 arasındadır. Lütfen çalışma saatlerimiz içinde tekrar deneyin.')
            return redirect('ana_sayfa')
        
        form = SiparisForm(request.POST)
        if form.is_valid():
            siparis = form.save(commit=False)
            siparis.toplam_fiyat = siparis.borek.fiyat * siparis.adet
            siparis.save()
            
            # Bildirimleri gönder
            notifications = send_order_notifications(siparis)
            
            messages.success(request, 'Siparişiniz başarıyla alındı! En kısa sürede sizinle iletişime geçeceğiz.')
            return redirect('ana_sayfa')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    return redirect('ana_sayfa')


def iletisim_gonder(request):
    """İletişim formu gönderme"""
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız alındı! En kısa sürede dönüş yapacağız.')
            return redirect('ana_sayfa')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    return redirect('ana_sayfa')
