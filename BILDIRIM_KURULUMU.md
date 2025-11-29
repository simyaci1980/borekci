# 📧 E-posta ve Telegram Bildirim Kurulumu

Sipariş geldiğinde otomatik bildirim almak için bu adımları takip edin.

## 1️⃣ Gmail Kurulumu (E-posta Bildirimleri)

### Adım 1: Gmail Uygulama Şifresi Oluşturma

1. Google hesabınıza gidin: https://myaccount.google.com/
2. Sol menüden **"Güvenlik"** seçin
3. **"2 Adımlı Doğrulama"** açık olmalı (değilse açın)
4. Aşağı kaydırın, **"Uygulama şifreleri"** bölümüne tıklayın
5. **"Uygulama seçin"** → "Diğer (Özel ad)" seçin
6. İsim yazın: "Börek Sitesi"
7. **"Oluştur"** butonuna tıklayın
8. Çıkan 16 haneli şifreyi kopyalayın (boşluksuz)

### Adım 2: settings.py Dosyasını Düzenleme

`borek_sitesi/settings.py` dosyasını açın ve şu satırları bulun:

```python
EMAIL_HOST_USER = 'sizin-email@gmail.com'  # Buraya Gmail adresinizi yazın
EMAIL_HOST_PASSWORD = 'uygulama-sifresi'  # Buraya Gmail uygulama şifrenizi yazın
DEFAULT_FROM_EMAIL = 'sizin-email@gmail.com'

ADMIN_EMAIL = 'sizin-email@gmail.com'  # Siparişlerin geleceği e-posta
```

**Değiştirin:**
- `sizin-email@gmail.com` → Gmail adresiniz (örn: `ahmet@gmail.com`)
- `uygulama-sifresi` → Oluşturduğunuz 16 haneli şifre

**Örnek:**
```python
EMAIL_HOST_USER = 'ahmet@gmail.com'
EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'  # 16 haneli uygulama şifresi
DEFAULT_FROM_EMAIL = 'ahmet@gmail.com'
ADMIN_EMAIL = 'ahmet@gmail.com'
```

## 2️⃣ Telegram Bot Kurulumu (Anında Bildirimler)

### Adım 1: Telegram Bot Oluşturma

1. Telegram'ı açın
2. **@BotFather** kullanıcısını arayın ve başlatın
3. `/newbot` komutunu gönderin
4. Bot için bir isim verin (örn: "Börek Siparişleri")
5. Bot için kullanıcı adı verin (örn: "borek_siparis_bot")
6. BotFather size **TOKEN** verecek (örn: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
7. Bu token'ı kopyalayın ve kaydedin

### Adım 2: Chat ID Bulma

1. Telegram'da kendi botunuzu arayın (verdiğiniz kullanıcı adı ile)
2. Bota `/start` mesajı gönderin
3. Tarayıcıda şu linke gidin (TOKEN yerine kendi tokeninizi yazın):
   ```
   https://api.telegram.org/botTOKENINIZ/getUpdates
   ```
   Örnek:
   ```
   https://api.telegram.org/bot123456789:ABCdefGHIjklMNOpqrsTUVwxyz/getUpdates
   ```

4. Açılan sayfada `"chat":{"id":123456789` gibi bir kısım göreceksiniz
5. Bu sayıyı (chat id) kopyalayın

### Adım 3: settings.py Dosyasını Düzenleme

`borek_sitesi/settings.py` dosyasında şu satırları bulun:

```python
TELEGRAM_BOT_TOKEN = 'bot-token-buraya'  # Telegram Bot Token
TELEGRAM_CHAT_ID = 'chat-id-buraya'  # Telegram Chat ID
```

**Değiştirin:**
```python
TELEGRAM_BOT_TOKEN = '123456789:ABCdefGHIjklMNOpqrsTUVwxyz'  # Sizin token
TELEGRAM_CHAT_ID = '123456789'  # Sizin chat id
```

## 3️⃣ Test Etme

1. Sunucuyu yeniden başlatın:
   ```bash
   python manage.py runserver
   ```

2. Siteden test siparişi verin

3. Kontrol edin:
   - ✅ Gmail'e e-posta geldi mi?
   - ✅ Telegram'a mesaj geldi mi?

## 🔧 Sorun Giderme

### E-posta gelmiyor:
- Gmail uygulama şifresini doğru kopyaladınız mı?
- 2 Adımlı Doğrulama açık mı?
- Terminal'de hata mesajı var mı?

### Telegram mesajı gelmiyor:
- Bot token doğru mu?
- Chat ID doğru mu?
- Bota `/start` mesajı gönderdiniz mi?

### Test için konsol çıktısı:
Sipariş verildiğinde terminalde "E-posta gönderilemedi" veya "Telegram mesajı gönderilemedi" gibi mesajlar görürsünüz.

## 📱 Bildirim Özellikleri

Her sipariş geldiğinde şu bilgiler gelir:

📧 **E-posta:**
- Müşteri adı, telefon, e-posta
- Sipariş detayları (ürün, adet, fiyat)
- Teslimat adresi
- Sipariş notu
- Sipariş zamanı

📱 **Telegram:**
- Kısa ve öz bilgiler
- Anında bildirim
- Her yerden erişim

---

**Artık hiçbir siparişi kaçırmazsınız!** 🎉
