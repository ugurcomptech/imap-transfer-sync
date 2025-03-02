# OfflineIMAP Toplu Senkronizasyon Yapılandırması

Bu betik, `accounts.txt` dosyasındaki kullanıcı bilgilerini okuyarak `offlineimaprc` yapılandırma dosyasını otomatik olarak oluşturur. Bu sayede birden fazla IMAP hesabını senkronize etmek için kullanılabilir.

## Kullanım Adımları

1. **Gerekli Bağımlılıkları Kur**
   
   OfflineIMAP'in sisteminde kurulu olduğundan emin ol:
   
   ```bash
   sudo apt update && sudo apt install offlineimap
   ```

2. **Hesap Bilgilerini Tanımla**
   
   `accounts.txt` adlı dosyayı aşağıdaki formatta oluştur:
   
   ```txt
   source_user1 source_pass1 dest_user1 dest_pass1
   source_user2 source_pass2 dest_user2 dest_pass2
   ```
   
   Her satır, bir kaynaktan bir hedefe aktarılacak IMAP hesaplarını temsil eder.

3. **Betiği Çalıştır**
   
   Betiği çalıştırarak `offlineimaprc` dosyasını oluştur:
   
   ```bash
   python generate_offlineimaprc.py
   ```
   
   Çalıştırıldıktan sonra `offlineimaprc` dosyası oluşturulacaktır.

4. **Oluşturulan offlineimaprc Dosyasını İncele**
   
   Aşağıdaki komutla içeriğini kontrol edebilirsin:
   
   ```bash
   cat offlineimaprc
   ```

5. **Dosya İzinlerini Güvenli Hale Getir**
   
   Şifrelerin açık şekilde yer aldığı bu dosyanın güvenliğini sağlamak için:
   
   ```bash
   chmod 600 offlineimaprc
   ```

6. **OfflineIMAP'i Çalıştır**
   
   Tüm hesapları senkronize etmek için aşağıdaki komutu kullan:
   
   ```bash
   offlineimap -c offlineimaprc
   ```

## Yapılandırma Açıklaması

- **SSL Sertifika Bilgileri**: Betik, `iRedMail` sertifikasını kullanacak şekilde yapılandırılmıştır. Gerekirse `SSL_CERT_FILE` ve `SSL_FINGERPRINT` değişkenlerini güncelleyebilirsin.
- **Toplu Hesap Yönetimi**: Betik, `accounts.txt` dosyasını okuyarak her hesap için ayrı bir `Account` ve `Repository` oluşturur.
- **Güvenlik Önlemleri**: Oluşturulan `offlineimaprc` dosyasına yalnızca sahibinin erişebilmesi için `chmod 600` uygulanır.

## Örnek offlineimaprc Çıktısı

```ini
[general]
accounts = transfer_1, transfer_2

[Account transfer_1]
localrepository = source_1
remoterepository = destination_1

[Repository source_1]
type = IMAP
remotehost = imail.ugurcomptech.net.tr
remoteuser = user1@example.com
remotepass = password1
ssl = yes
sslcacertfile = /etc/ssl/certs/iRedMail.crt
sslcertck = no
sslfingerprint = C4:9B:B1:8C:73:76:53:EA:42:15:33:46:46:EE:CF:D6:AC:37:8C:FB

[Repository destination_1]
type = IMAP
remotehost = imail.ugurcomptech.net.tr
remoteuser = user1backup@example.com
remotepass = password2
ssl = yes
sslcacertfile = /etc/ssl/certs/iRedMail.crt
sslcertck = no
sslfingerprint = C4:9B:B1:8C:73:76:53:EA:42:15:33:46:46:EE:CF:D6:AC:37:8C:FB
```

Bu yapılandırma ile hesaplar arasında IMAP senkronizasyonu güvenli ve otomatik bir şekilde gerçekleştirilebilir.

