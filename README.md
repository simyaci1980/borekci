# Börek Satış Sitesi

Django ile geliştirilmiş, modern ve responsive tek sayfalık börek satış sitesi.

## 🚀 Proje Özellikleri

- **Tek Sayfalık Modern Tasarım**: Kullanıcı dostu, responsive tasarım
- **Ürün Yönetimi**: Admin panelinden börek çeşitleri ekleyip düzenleyebilme
- **Sipariş Sistemi**: Müşterilerin online sipariş verebilmesi
- **İletişim Formu**: Müşteri mesajlarını yönetme
- **Admin Panel**: Siparişleri ve ürünleri yönetme

## 📋 Kurulum

Proje zaten kurulu ve çalışır durumda!

## 🔑 Admin Paneli

- **URL**: http://127.0.0.1:8000/admin/
- **Kullanıcı Adı**: admin
- **Şifre**: admin123

## 🌐 Kullanım

1. **Ana Sayfa**: http://127.0.0.1:8000/
2. **Admin Panel**: http://127.0.0.1:8000/admin/

### Admin Panelinden Yapabilecekleriniz:

1. **Börek Çeşitleri Ekleyin**:
   - Admin paneline giriş yapın
   - "Börek Çeşitleri" bölümüne gidin
   - "Ekle" butonuna tıklayın
   - Börek adı, açıklama, fiyat ve resim ekleyin

2. **Siparişleri Yönetin**:
   - Gelen siparişleri görüntüleyin
   - Sipariş durumlarını güncelleyin (Yeni, Hazırlanıyor, Teslim Edildi)
   - Müşteri bilgilerini görün

3. **İletişim Mesajlarını Takip Edin**:
   - Gelen mesajları okuyun
   - Mesajları "okundu" olarak işaretleyin

## 📁 Proje Yapısı

```
borek_sitesi/
├── ana_sayfa/              # Ana uygulama
│   ├── models.py          # Veritabanı modelleri
│   ├── views.py           # View fonksiyonları
│   ├── forms.py           # Form sınıfları
│   ├── admin.py           # Admin panel ayarları
│   └── templates/         # HTML şablonları
├── static/                 # CSS, JS dosyaları
│   ├── css/
│   └── js/
├── media/                  # Yüklenen resimler
└── manage.py
```

## 🎨 Özellikler

### Anasayfa Bölümleri:
- **Hero Section**: Çarpıcı karşılama bölümü
- **Özellikler**: Doğal malzemeler, ev yapımı, hızlı teslimat
- **Ürünler**: Börek çeşitlerinin listesi
- **Hakkımızda**: İşletme bilgileri
- **Sipariş Formu**: Online sipariş verme
- **İletişim**: İletişim bilgileri ve mesaj formu

### Teknik Özellikler:
- Responsive tasarım (mobil uyumlu)
- Modern CSS animasyonları
- Form validasyonu
- Otomatik fiyat hesaplama
- Resim yükleme desteği
- Admin paneli ile kolay yönetim

## 📱 Instagram Entegrasyonu İçin

1. Ürün resimlerinizi admin panelinden ekleyin
2. Instagram reklamlarınızda sitenizin linkini paylaşın
3. Müşteriler direkt sipariş verebilir
4. Siparişleri admin panelinden takip edin

## 🛠️ Geliştirme

Sunucuyu başlatmak için:
```bash
python manage.py runserver
```

## 📝 Notlar

- İlk kullanımda admin panelinden ürünlerinizi ekleyin
- İletişim bilgilerini (telefon, email, Instagram) templates/ana_sayfa/index.html dosyasından güncelleyebilirsiniz
- Sitenin renklerini ve stilini static/css/style.css dosyasından özelleştirebilirsiniz

## 🎯 Sonraki Adımlar

1. Admin panelinden börek çeşitlerinizi ekleyin
2. Gerçek ürün resimlerinizi yükleyin
3. İletişim bilgilerinizi güncelleyin
4. Instagram reklamlarınızı başlatın!

---

**İyi satışlar! 🥟**
