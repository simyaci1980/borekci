from django import forms
from .models import Siparis, Iletisim


class SiparisForm(forms.ModelForm):
    class Meta:
        model = Siparis
        fields = ['telefon', 'adres', 'borek', 'adet', 'not_mesaj']
        widgets = {
            'telefon': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '05XX XXX XX XX', 
                'required': True,
                'pattern': '[0-9]{10,11}',
                'title': 'Lütfen geçerli bir telefon numarası girin (10-11 hane)',
                'minlength': '10',
                'maxlength': '11'
            }),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Teslimat adresiniz (mahalle, sokak, bina no, daire)', 'required': True}),
            'borek': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'adet': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'value': 1, 'required': True}),
            'not_mesaj': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Özel notunuz varsa yazın (opsiyonel)', 'required': False}),
        }
    
    def clean_telefon(self):
        telefon = self.cleaned_data.get('telefon')
        # Sadece rakamları al
        telefon_rakamlar = ''.join(filter(str.isdigit, telefon))
        
        if len(telefon_rakamlar) < 10:
            raise forms.ValidationError('Telefon numarası en az 10 hane olmalıdır.')
        
        if len(telefon_rakamlar) > 11:
            raise forms.ValidationError('Telefon numarası en fazla 11 hane olmalıdır.')
        
        return telefon


class IletisimForm(forms.ModelForm):
    class Meta:
        model = Iletisim
        fields = ['ad_soyad', 'email', 'telefon', 'mesaj']
        widgets = {
            'ad_soyad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ornek@email.com'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '05XX XXX XX XX'}),
            'mesaj': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mesajınız'}),
        }
