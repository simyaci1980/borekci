from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BorekCesidi, Siparis, Iletisim
from .forms import SiparisForm, IletisimForm
from .notifications import send_order_notifications


def ana_sayfa(request):
    """Ana sayfa - Tek sayfalık börek satış sitesi"""
    borekler = BorekCesidi.objects.filter(aktif=True)
    siparis_form = SiparisForm()
    iletisim_form = IletisimForm()
    
    context = {
        'borekler': borekler,
        'siparis_form': siparis_form,
        'iletisim_form': iletisim_form,
    }
    return render(request, 'ana_sayfa/index.html', context)


def siparis_olustur(request):
    """Sipariş oluşturma"""
    if request.method == 'POST':
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
