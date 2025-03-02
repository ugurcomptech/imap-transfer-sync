import os

# Kullanıcı bilgileri dosyası
ACCOUNTS_FILE = "accounts.txt"
OUTPUT_FILE = os.path.expanduser("~/.offlineimaprc")  # HOME dizinine yazacak

# SSL Sertifika bilgileri (gerekirse değiştir)
SSL_CERT_FILE = ""
SSL_FINGERPRINT = ""

# offlineimaprc başlığı
config = """[general]
accounts = {}
"""

accounts = []
repo_configs = ""

# accounts.txt dosyasını oku ve yapılandırmayı oluştur
with open(ACCOUNTS_FILE, "r") as f:
    for i, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) != 4:
            continue  # Hatalı satırları atla

        source_user, source_pass, dest_user, dest_pass = parts
        account_name = f"transfer_{i+1}"
        accounts.append(account_name)

        repo_configs += f"""
[Account {account_name}]
localrepository = source_{i+1}
remoterepository = destination_{i+1}

[Repository source_{i+1}]
type = IMAP
remotehost = 
remoteuser = {source_user}
remotepass = {source_pass}
ssl = yes
sslcacertfile = {SSL_CERT_FILE}
sslcertck = no
sslfingerprint = {SSL_FINGERPRINT}

[Repository destination_{i+1}]
type = IMAP
remotehost = 
remoteuser = {dest_user}
remotepass = {dest_pass}
ssl = yes
sslcacertfile = {SSL_CERT_FILE}
sslcertck = no
sslfingerprint = {SSL_FINGERPRINT}
"""

# offlineimaprc dosyasını HOME dizinine yaz
config = config.format(", ".join(accounts)) + repo_configs

with open(OUTPUT_FILE, "w") as f:
    f.write(config)

# Dosya izinlerini güvenli hale getir
os.chmod(OUTPUT_FILE, 0o600)

print(f"✅ '{OUTPUT_FILE}' başarıyla oluşturuldu. Şimdi offlineimap çalıştırabilirsin!")
