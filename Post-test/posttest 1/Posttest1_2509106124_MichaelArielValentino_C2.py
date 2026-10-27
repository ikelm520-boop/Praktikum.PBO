from datetime import datetime


class User:
    nama_instansi = "Osaka Bluteon Volleyball Club" 
    total_user = 0                   
    role_valid = ["pelatih", "pemain"]   

    def __init__(self, nama, email, password, role, no_telepon):
        self.nama = nama
        self.email = email if User.validasi_email(email) else "email_tidak_valid@x.com"
        self.role = role if role in User.role_valid else "pemain"
        self.no_telepon = no_telepon

        self.__password = None
        self.password = password  

        User.total_user += 1
        self.id_user = User.total_user

    @property
    def password(self):
        return "********" 

    @password.setter
    def password(self, value):
        if not value or len(str(value)) < 6:
            print(f"[GAGAL] Password '{self.nama}' ditolak: minimal 6 karakter.")
            return
        self.__password = value

    def tampilkan_info(self):
        print(f"ID User    : {self.id_user}")
        print(f"Nama       : {self.nama}")
        print(f"Email      : {self.email}")
        print(f"Role       : {self.role.upper()}")
        print(f"No. Telp   : {self.no_telepon}")
        print(f"Instansi   : {User.nama_instansi}")

    @classmethod
    def dari_dict(cls, data: dict):
        return cls(
            data.get("nama"),
            data.get("email"),
            data.get("password"),
            data.get("role"),
            data.get("no_telepon"),
        )

    @classmethod
    def ubah_nama_instansi(cls, nama_baru):
        cls.nama_instansi = nama_baru

    @staticmethod
    def validasi_email(email):
        return isinstance(email, str) and "@" in email


class Jadwal:
    total_jadwal = 0
    jenis_valid = ["latihan", "pertandingan"]
    lokasi_default = "GOR Osaka Bluteon (Home)"

    def __init__(self, jenis_sesi, tanggal, kuota, lokasi=None, status="terbuka"):
        Jadwal.total_jadwal += 1
        self.id_jadwal = Jadwal.total_jadwal

        self.jenis_sesi = jenis_sesi if jenis_sesi in Jadwal.jenis_valid else "latihan"
        self.tanggal = tanggal
        self.lokasi = lokasi if lokasi else Jadwal.lokasi_default
        self.status = status
        self.jumlah_pendaftar = 0

        self.__kuota = 0
        self.kuota = kuota 

    @property
    def kuota(self):
        return self.__kuota

    @kuota.setter
    def kuota(self, value):
        if not isinstance(value, int) or value < 0:
            print(f"[GAGAL] Kuota jadwal '{self.jenis_sesi}' ditolak: harus angka >= 0.")
            return
        self.__kuota = value

    def tampilkan_jadwal(self):
        print(f"ID Jadwal  : {self.id_jadwal}")
        print(f"Jenis      : {self.jenis_sesi.upper()}")
        print(f"Tanggal    : {self.tanggal}")
        print(f"Lokasi     : {self.lokasi}") 
        print(f"Kuota      : {self.jumlah_pendaftar}/{self.kuota}")
        print(f"Status     : {self.status}")

    def tambah_pendaftar(self):
        if self.jumlah_pendaftar < self.__kuota:
            self.jumlah_pendaftar += 1
            return True
        return False

    def kurangi_pendaftar(self):
        if self.jumlah_pendaftar > 0:
            self.jumlah_pendaftar -= 1

    @classmethod
    def dari_dict(cls, data: dict):
        return cls(
            data.get("jenis_sesi"),
            data.get("tanggal"),
            data.get("kuota", 0),
            data.get("lokasi"), 
        )

    @staticmethod
    def validasi_format_tanggal(tanggal_str, fmt="%Y-%m-%d"):
        try:
            datetime.strptime(tanggal_str, fmt)
            return True
        except (ValueError, TypeError):
            return False


class Pendaftaran:
    total_pendaftaran = 0
    status_valid = ["menunggu", "dikonfirmasi", "ditolak"]

    def __init__(self, pemain: User, jadwal: Jadwal):
        Pendaftaran.total_pendaftaran += 1
        self.id_pendaftaran = Pendaftaran.total_pendaftaran

        self.pemain = pemain 
        self.jadwal = jadwal 
        self.waktu_daftar = datetime.now().strftime("%Y-%m-%d %H:%M")

        self.__status = "menunggu"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value not in Pendaftaran.status_valid:
            print(f"[GAGAL] Status '{value}' tidak valid.")
            return
        self.__status = value

    def konfirmasi(self):
        if self.jadwal.tambah_pendaftar():
            self.status = "dikonfirmasi"
            print(f"[OK] Pendaftaran #{self.id_pendaftaran} ({self.pemain.nama}) dikonfirmasi untuk "
                  f"{self.jadwal.jenis_sesi.upper()} di {self.jadwal.lokasi}.")
        else:
            self.status = "ditolak"
            print(f"[GAGAL] Kuota '{self.jadwal.jenis_sesi}' penuh. Pendaftaran #{self.id_pendaftaran} ditolak.")

    def batalkan(self):
        if self.__status == "dikonfirmasi":
            print(f"[GAGAL] Pendaftaran #{self.id_pendaftaran} sudah dikonfirmasi, tidak bisa dibatalkan sendiri.")
            return False
        self.status = "ditolak"
        print(f"[INFO] Pendaftaran #{self.id_pendaftaran} dibatalkan oleh pemain.")
        return True

    def tampilkan(self):
        print(f"ID Pendaftaran : {self.id_pendaftaran}")
        print(f"Pemain         : {self.pemain.nama}")
        print(f"Jadwal         : {self.jadwal.jenis_sesi.upper()} ({self.jadwal.tanggal})")
        print(f"Lokasi         : {self.jadwal.lokasi}")
        print(f"Status         : {self.status.upper()}")

    @classmethod
    def buat_pendaftaran(cls, pemain, jadwal):
        if pemain.role != "pemain":
            print(f"[GAGAL] {pemain.nama} berrole '{pemain.role}', bukan pemain. Tidak bisa mendaftar.")
            return None
        return cls(pemain, jadwal)


class Pembayaran:
    total_pembayaran = 0
    metode_valid = ["cash", "transfer", "qris"]
    status_valid = ["belum lunas", "lunas"]

    def __init__(self, pendaftaran: Pendaftaran, jumlah, metode):
        Pembayaran.total_pembayaran += 1
        self.id_pembayaran = Pembayaran.total_pembayaran

        self.pendaftaran = pendaftaran 
        self.metode = metode if metode in Pembayaran.metode_valid else "cash"

        self.__jumlah = 0
        self.jumlah = jumlah 
        self.__status_bayar = "belum lunas"

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            print("[GAGAL] Jumlah pembayaran ditolak: tidak boleh negatif.")
            return
        self.__jumlah = value

    @property
    def status_bayar(self):
        return self.__status_bayar

    @status_bayar.setter
    def status_bayar(self, value):
        if value not in Pembayaran.status_valid:
            print(f"[GAGAL] Status bayar '{value}' tidak valid.")
            return
        self.__status_bayar = value

    def verifikasi(self):
        self.status_bayar = "lunas"
        print(f"[OK] Pembayaran #{self.id_pembayaran} Rp{self.jumlah:,.0f} milik "
              f"{self.pendaftaran.pemain.nama} telah diverifikasi (LUNAS).")

    def tampilkan(self):
        print(f"ID Pembayaran  : {self.id_pembayaran}")
        print(f"Pendaftaran    : #{self.pendaftaran.id_pendaftaran} ({self.pendaftaran.pemain.nama})")
        print(f"Sesi           : {self.pendaftaran.jadwal.jenis_sesi.upper()}")
        print(f"Jumlah         : Rp{self.jumlah:,.0f}")
        print(f"Metode         : {self.metode.upper()}")
        print(f"Status Bayar   : {self.status_bayar.upper()}")


if __name__ == "__main__":

    print("=" * 50)
    print(" SISTEM MANAJEMEN TIM VOLI OSAKA BLUTEON")
    print("=" * 50)

    print("\n--- [1] Membuat Objek User (Data Asli) ---")
    coach = User("Laurent Tillie", "tillie@bluteon.jp", "osaka123", "pelatih", "+81801")
    
    p1 = User("Yuji Nishida", "nishida@bluteon.jp", "yuji123", "pemain", "+81802")
    
    p2_data = {
        "nama": "Masahiro Sekita",
        "email": "sekita@bluteon.jp",
        "password": "sekita123",
        "role": "pemain",
        "no_telepon": "+81803",
    }
    p2 = User.dari_dict(p2_data)
    p3 = User("Akihiro Yamauchi", "yamauchi@bluteon.jp", "yamauchi123", "pemain", "+81804")

    coach.tampilkan_info()
    print("-")
    p1.tampilkan_info()

    print("\n--- [2] Membuat Objek Jadwal (Home & Away) ---")
    
    jadwal_home = Jadwal("latihan", "2024-06-01", kuota=2)
    
    jadwal_away = Jadwal.dari_dict({
        "jenis_sesi": "pertandingan",
        "tanggal": "2024-06-10",
        "kuota": 1,
        "lokasi": "Suntory Sunbirds Arena (Away)" 
    })

    jadwal_home.tampilkan_jadwal()
    print("-")
    jadwal_away.tampilkan_jadwal()

    print("\n--- [3] Proses Pendaftaran Pemain ---")
    daftar1 = Pendaftaran.buat_pendaftaran(p1, jadwal_home) 
    daftar2 = Pendaftaran.buat_pendaftaran(p2, jadwal_home) 
    daftar3 = Pendaftaran.buat_pendaftaran(p3, jadwal_home) 

    print("\nPelatih mengonfirmasi Pendaftaran (Cek Kuota):")
    if daftar1: daftar1.konfirmasi() 
    if daftar2: daftar2.konfirmasi() 
    if daftar3: daftar3.konfirmasi() 

    print("\nRingkasan Status Pendaftaran:")
    if daftar1: daftar1.tampilkan()
    print("-")
    if daftar3: daftar3.tampilkan() 

    print("\n--- [4] Proses Pembayaran Iuran ---")
    bayar1 = Pembayaran(daftar1, 150000, "qris")
    bayar1.tampilkan()
    
    print("\nPelatih memverifikasi pembayaran:")
    bayar1.verifikasi() 
    bayar1.tampilkan()

    print("\n--- [5] Uji Validasi & Encapsulation (Setter) ---")
    
    print("> Ganti Password Nishida (terlalu pendek):")
    p1.password = "123" 
    
    print("\n> Set Kuota Jadwal Negatif:")
    jadwal_home.kuota = -10 

    print("\n> Set Jumlah Pembayaran Negatif:")
    bayar1.jumlah = -50000 

    print("\n--- [6] Demo Fitur Pembatalan Pendaftaran ---")
    daftar_away = Pendaftaran.buat_pendaftaran(p3, jadwal_away)
    
    print("\nStatus sebelum dibatalkan:")
    daftar_away.tampilkan() 
    
    print("\nPemain membatalkan pendaftaran:")
    daftar_away.batalkan() 
    
    print("\nStatus akhir pendaftaran away:")
    daftar_away.tampilkan() 

    print("\n--- [7] Ringkasan Statistik Sistem (Atribut Kelas) ---")
    print(f"Total User Terdaftar   : {User.total_user}")
    print(f"Total Jadwal Dibuat    : {Jadwal.total_jadwal}")
    print(f"Total Pendaftaran      : {Pendaftaran.total_pendaftaran}")
    print(f"Total Record Pembayaran: {Pembayaran.total_pembayaran}")
    print(f"Nama Instansi Saat Ini : {User.nama_instansi}")