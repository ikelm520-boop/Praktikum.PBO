import time

# ==============================================================
#                    SISTEM TOP UP GAME
# ==============================================================
# GANTI dua nilai di bawah ini sesuai data kamu:
USERNAME_BENAR = "budi"   # <- nama panggilan kamu
PASSWORD_BENAR = "23"     # <- 2 digit NIM kamu
# ==============================================================

LEBAR = 50


def garis(char="="):
    print(char * LEBAR)


def judul(teks):
    garis("=")
    print(teks.center(LEBAR))
    garis("=")


def rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")


def loading(teks):
    print(teks, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()


# ----------------------- 1. LOGIN -----------------------------
judul("🎮  SISTEM TOP UP GAME  🎮")
print("LOGIN".center(LEBAR))
garis("-")
username = input("Username (nama panggilan) : ").strip()
password = input("Password (2 digit NIM)    : ").strip()
garis("-")

# ----------------------- 2. VALIDASI LOGIN --------------------
if username == USERNAME_BENAR and password == PASSWORD_BENAR:
    print("✅ Login Berhasil")
    print(f"Selamat datang, {username}!")
else:
    print("❌ Login Gagal")
    exit()  # program langsung berakhir tanpa menu top up

# ----------------------- 3. INPUT DATA TOP UP -----------------
print()
judul("MENU TOP UP")

id_player = input("ID Player                                  : ").strip()

# Nama Game
print("\nPilihan Game : Genshin Impact / Minecraft / Mobile Legends")
while True:
    nama_game = input("Nama Game                                  : ").strip().title()
    if nama_game in ("Genshin Impact", "Minecraft", "Mobile Legends"):
        break
    print("⚠️  Game tidak tersedia, coba lagi.")

# Kategori Top Up
print("\nPilihan Kategori : Kecil / Menengah / Besar")
while True:
    kategori = input("Kategori Top Up                            : ").strip().title()
    if kategori in ("Kecil", "Menengah", "Besar"):
        break
    print("⚠️  Kategori tidak valid, coba lagi.")

# Metode Pembayaran
print("\nPilihan Metode : Pulsa / E-Wallet")
while True:
    metode = input("Metode Pembayaran                           : ").strip().title()
    if metode in ("Pulsa", "E-Wallet"):
        break
    print("⚠️  Metode tidak valid, coba lagi.")

# ----------------------- 4. HARGA DASAR (IF/ELIF/ELSE) --------
if kategori == "Kecil":
    harga_dasar = 15000
elif kategori == "Menengah":
    harga_dasar = 50000
else:  # Besar
    harga_dasar = 150000

# ----------------------- 5. BIAYA ADMIN (TERNARY) -------------
biaya_admin = 2500 if metode == "Pulsa" else 500

# ----------------------- 6. TOTAL BAYAR -----------------------
total_bayar = harga_dasar + biaya_admin

# ----------------------- POIN PLUS: PEMBAYARAN ----------------
print()
loading("Menghitung tagihan")
garis("-")
print(f"Harga Top Up  : {rupiah(harga_dasar)}")
print(f"Biaya Admin   : {rupiah(biaya_admin)}")
print(f"TOTAL BAYAR   : {rupiah(total_bayar)}")
garis("-")

while True:
    try:
        uang_bayar = int(input("Masukkan nominal uang (angka)  : Rp "))
        break
    except ValueError:
        print("⚠️  Masukkan angka saja, tanpa titik/koma.")

if uang_bayar < total_bayar:
    print()
    print("❌ Transaksi Gagal Saldo tidak mencukupi")
    print(f"   Kurang: {rupiah(total_bayar - uang_bayar)}")
else:
    kembalian = uang_bayar - total_bayar

    # ----------------------- 7. STRUK PEMBELIAN ---------------
    print()
    loading("Memproses transaksi")
    print()
    garis("=")
    print("STRUK PEMBELIAN TOP UP".center(LEBAR))
    print(f"({time.strftime('%d-%m-%Y %H:%M:%S')})".center(LEBAR))
    garis("=")
    print(f"{'ID Player':<20}: {id_player}")
    print(f"{'Nama Game':<20}: {nama_game}")
    print(f"{'Kategori Top Up':<20}: {kategori}")
    print(f"{'Metode Pembayaran':<20}: {metode}")
    garis("-")
    print(f"{'Harga Top Up':<20}: {rupiah(harga_dasar)}")
    print(f"{'Biaya Admin':<20}: {rupiah(biaya_admin)}")
    print(f"{'Total Bayar':<20}: {rupiah(total_bayar)}")
    print(f"{'Uang Dibayar':<20}: {rupiah(uang_bayar)}")
    print(f"{'Kembalian':<20}: {rupiah(kembalian)}")
    garis("=")
    print("Terima kasih, selamat bermain! 🎉".center(LEBAR))
    garis("=")