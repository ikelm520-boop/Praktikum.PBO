from datetime import datetime

class User:
    nama_instansi = 'Osaka Bluteon Volleyball Club'
    total_user = 0
    role_valid = ['pelatih', 'pemain']

    def __init__(self, nama, email, password, no_telepon, role='pemain'):
        User.total_user += 1
        self._id_user = User.total_user
        self.nama = nama
        self.email = email if User.validasi_email(email) else 'email_tidak_valid@x.com'
        self.no_telepon = no_telepon
        self.role = role if role in User.role_valid else 'pemain'
        self.__password = None
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not value or len(str(value)) < 6:
            print(f"[GAGAL] Password '{self.nama}' ditolak: minimal 6 karakter.")
            return
        self.__password = value
        print(f'[OK] Password untuk {self.nama} berhasil diset/diubah.')

    def tampilkan_info(self):
        print(f'ID User    : {self._id_user}')
        print(f'Nama       : {self.nama}')
        print(f'Email      : {self.email}')
        print(f'Role       : {self.role.upper()}')
        print(f'No. Telp   : {self.no_telepon}')
        print(f'Instansi   : {User.nama_instansi}')

    @classmethod
    def ubah_nama_instansi(cls, nama_baru):
        cls.nama_instansi = nama_baru

    @staticmethod
    def validasi_email(email):
        return isinstance(email, str) and '@' in email and ('.' in email.split('@')[-1])

class Pelatih(User):

    def __init__(self, nama, email, password, no_telepon, spesialisasi):
        super().__init__(nama, email, password, no_telepon, role='pelatih')
        self.spesialisasi = spesialisasi

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f'Spesialisasi: {self.spesialisasi}')
        print(f'(_id_user protected diakses langsung dari subclass: {self._id_user})')

    @classmethod
    def dari_dict(cls, data: dict):
        return cls(data.get('nama'), data.get('email'), data.get('password'), data.get('no_telepon'), data.get('spesialisasi'))

    def buat_jadwal(self, jenis_sesi, tanggal, kuota, lokasi=None):
        jadwal = Jadwal(jenis_sesi, tanggal, kuota, lokasi, self)
        print(f"[PELATIH] {self.nama} membuat jadwal '{jenis_sesi}' pada {tanggal}.")
        return jadwal

    def rekrut_pemain(self, tim, pemain):
        tim.tambah_pemain(pemain)

    def konfirmasi_pendaftaran(self, pendaftaran):
        pendaftaran.konfirmasi()

    def verifikasi_pembayaran(self, pembayaran):
        pembayaran.verifikasi()

class Pemain(User):

    def __init__(self, nama, email, password, no_telepon, posisi, nomor_punggung):
        super().__init__(nama, email, password, no_telepon, role='pemain')
        self.posisi = posisi
        self.nomor_punggung = nomor_punggung

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f'Posisi     : {self.posisi}')
        print(f'No. Punggung: {self.nomor_punggung}')

    @classmethod
    def dari_dict(cls, data: dict):
        return cls(data.get('nama'), data.get('email'), data.get('password'), data.get('no_telepon'), data.get('posisi'), data.get('nomor_punggung'))

    def daftar_sesi(self, jadwal):
        pendaftaran = Pendaftaran.buat_pendaftaran(self, jadwal)
        if pendaftaran:
            print(f"[PEMAIN] {self.nama} mendaftar ke sesi '{jadwal.jenis_sesi}' ({jadwal.tanggal}).")
        return pendaftaran

    def bayar_iuran(self, pendaftaran, jumlah, metode):
        return Pembayaran(pendaftaran, jumlah, metode)

class Jadwal:
    total_jadwal = 0
    jenis_valid = ['latihan', 'pertandingan']
    lokasi_default = 'Panasonic Arena (Home)'

    def __init__(self, jenis_sesi, tanggal, kuota, lokasi=None, pelatih_penanggungjawab=None, status='terbuka'):
        Jadwal.total_jadwal += 1
        self.id_jadwal = Jadwal.total_jadwal
        self.jenis_sesi = jenis_sesi if jenis_sesi in Jadwal.jenis_valid else 'latihan'
        self.tanggal = tanggal
        self.lokasi = lokasi if lokasi else Jadwal.lokasi_default
        self.status = status
        self.jumlah_pendaftar = 0
        self.pelatih_penanggungjawab = pelatih_penanggungjawab
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
        pj = self.pelatih_penanggungjawab.nama if self.pelatih_penanggungjawab else '-'
        print(f'ID Jadwal  : {self.id_jadwal}')
        print(f'Jenis      : {self.jenis_sesi.upper()}')
        print(f'Tanggal    : {self.tanggal}')
        print(f'Lokasi     : {self.lokasi}')
        print(f'Kuota      : {self.jumlah_pendaftar}/{self.kuota}')
        print(f'Status     : {self.status}')
        print(f'PJ Pelatih : {pj}')

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
        return cls(data.get('jenis_sesi'), data.get('tanggal'), data.get('kuota', 0), data.get('lokasi'), data.get('pelatih_penanggungjawab'))

    @staticmethod
    def validasi_format_tanggal(tanggal_str, fmt='%Y-%m-%d'):
        try:
            datetime.strptime(tanggal_str, fmt)
            return True
        except (ValueError, TypeError):
            return False

class Pendaftaran:
    total_pendaftaran = 0
    status_valid = ['menunggu', 'dikonfirmasi', 'ditolak']

    def __init__(self, pemain: 'Pemain', jadwal: 'Jadwal'):
        Pendaftaran.total_pendaftaran += 1
        self.id_pendaftaran = Pendaftaran.total_pendaftaran
        self.pemain = pemain
        self.jadwal = jadwal
        self.waktu_daftar = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.__status = 'menunggu'

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
            self.status = 'dikonfirmasi'
            print(f'[OK] Pendaftaran #{self.id_pendaftaran} ({self.pemain.nama}) dikonfirmasi untuk {self.jadwal.jenis_sesi.upper()} di {self.jadwal.lokasi}.')
        else:
            self.status = 'ditolak'
            print(f"[GAGAL] Kuota '{self.jadwal.jenis_sesi}' penuh. Pendaftaran #{self.id_pendaftaran} ditolak.")

    def batalkan(self):
        if self.__status == 'dikonfirmasi':
            print(f'[GAGAL] Pendaftaran #{self.id_pendaftaran} sudah dikonfirmasi, tidak bisa dibatalkan sendiri.')
            return False
        self.status = 'ditolak'
        print(f'[INFO] Pendaftaran #{self.id_pendaftaran} dibatalkan oleh pemain.')
        return True

    def tampilkan(self):
        print(f'ID Pendaftaran : {self.id_pendaftaran}')
        print(f'Pemain         : {self.pemain.nama}')
        print(f'Jadwal         : {self.jadwal.jenis_sesi.upper()} ({self.jadwal.tanggal})')
        print(f'Lokasi         : {self.jadwal.lokasi}')
        print(f'Status         : {self.status.upper()}')

    @classmethod
    def buat_pendaftaran(cls, pemain, jadwal):
        if not isinstance(pemain, Pemain):
            print(f'[GAGAL] {pemain.nama} bukan objek Pemain. Tidak bisa mendaftar.')
            return None
        return cls(pemain, jadwal)

    @staticmethod
    def validasi_status(status):
        return status in Pendaftaran.status_valid

class Pembayaran:
    total_pembayaran = 0
    metode_valid = ['cash', 'transfer', 'qris']
    status_valid = ['belum lunas', 'lunas']

    def __init__(self, pendaftaran: 'Pendaftaran', jumlah, metode):
        Pembayaran.total_pembayaran += 1
        self.id_pembayaran = Pembayaran.total_pembayaran
        self.pendaftaran = pendaftaran
        self.metode = metode if metode in Pembayaran.metode_valid else 'cash'
        self.__jumlah = 0
        self.jumlah = jumlah
        self.__status_bayar = 'belum lunas'

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            print('[GAGAL] Jumlah pembayaran ditolak: tidak boleh negatif.')
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
        self.status_bayar = 'lunas'
        print(f'[OK] Pembayaran #{self.id_pembayaran} ¥{self.jumlah:,.0f} milik {self.pendaftaran.pemain.nama} telah diverifikasi (LUNAS).')

    def tampilkan(self):
        print(f'ID Pembayaran  : {self.id_pembayaran}')
        print(f'Pendaftaran    : #{self.pendaftaran.id_pendaftaran} ({self.pendaftaran.pemain.nama})')
        print(f'Sesi           : {self.pendaftaran.jadwal.jenis_sesi.upper()}')
        print(f'Jumlah         : ¥{self.jumlah:,.0f}')
        print(f'Metode         : {self.metode.upper()}')
        print(f'Status Bayar   : {self.status_bayar.upper()}')

    @classmethod
    def buat_pembayaran(cls, pendaftaran, jumlah, metode):
        return cls(pendaftaran, jumlah, metode)

    @staticmethod
    def validasi_metode(metode):
        return metode in Pembayaran.metode_valid

class Kas:

    def __init__(self, nama_tim):
        self.nama_tim = nama_tim
        self.saldo = 0

    def tambah_dana(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f'[KAS] Dana kas tim {self.nama_tim} bertambah ¥{jumlah:,.0f}. Saldo sekarang: ¥{self.saldo:,.0f}')
        else:
            print('[KAS] Gagal menambah dana, jumlah harus lebih dari 0.')

    def tampilkan_saldo(self):
        print(f'[KAS] Saldo kas tim {self.nama_tim}: ¥{self.saldo:,.0f}')

class Tim:
    total_tim = 0
    nama_liga = 'SV.League Japan'

    def __init__(self, nama_tim, kota_asal):
        Tim.total_tim += 1
        self.id_tim = Tim.total_tim
        self.nama_tim = nama_tim
        self.kota_asal = kota_asal
        self.daftar_pemain = []
        self.__kas = Kas(nama_tim)

    def tambah_pemain(self, pemain):
        if isinstance(pemain, Pemain):
            self.daftar_pemain.append(pemain)
            print(f'[TIM] {pemain.nama} bergabung ke tim {self.nama_tim}.')
        else:
            print('[GAGAL] Hanya objek Pemain yang bisa ditambahkan ke tim.')

    def keluarkan_pemain(self, pemain):
        if pemain in self.daftar_pemain:
            self.daftar_pemain.remove(pemain)
            print(f'[TIM] {pemain.nama} keluar dari tim {self.nama_tim}, objek Pemain-nya tetap ada (tidak ikut terhapus).')

    def isi_kas(self, jumlah):
        self.__kas.tambah_dana(jumlah)

    def cek_kas(self):
        self.__kas.tampilkan_saldo()

    def tampilkan_tim(self):
        print(f'Tim          : {self.nama_tim} ({self.kota_asal})')
        print(f'Liga         : {Tim.nama_liga}')
        print(f'Jumlah Pemain: {len(self.daftar_pemain)}')
        for p in self.daftar_pemain:
            print(f'  - {p.nama} ({p.posisi}, #{p.nomor_punggung})')

if __name__ == '__main__':
    print('=' * 70)
    print(' SISTEM MANAJEMEN OSAKA BLUTEON VOLLEYBALL CLUB')
    print('=' * 70)
    print('\n--- [1] Membuat Objek Pelatih & Pemain (Subclass dari User) ---')
    pelatih1 = Pelatih('Laurent Tillie', 'laurent@osakabluteon.jp', 'coach123', '090xxxx', 'Head Coach & Taktik')
    pelatih2 = Pelatih.dari_dict({'nama': 'Toshiaki Kawai', 'email': 'kawai@osakabluteon.jp', 'password': 'kawai12345', 'no_telepon': '090yyyy', 'spesialisasi': 'Asisten Pelatih'})
    pemain1 = Pemain('Yuji Nishida', 'nishida@osakabluteon.jp', 'nishida11', '0801111', 'Opposite', 11)
    pemain2 = Pemain.dari_dict({'nama': 'Thomas Jaeschke', 'email': 'jaeschke@osakabluteon.jp', 'password': 'jaeschke8', 'no_telepon': '0802222', 'posisi': 'Outside Hitter', 'nomor_punggung': 8})
    pemain3 = Pemain('Akihiro Yamauchi', 'yamauchi@osakabluteon.jp', 'yamauchi13', '0803333', 'Middle Blocker', 13)
    
    print('\n--- [2] Polymorphism / Method Overriding: tampilkan_info() ---')
    for u in (pelatih1, pelatih2, pemain1, pemain2, pemain3):
        u.tampilkan_info()
        print('-')
    User.ubah_nama_instansi('Osaka Bluteon Volleyball Club (Pro Team)')
    print(f'Nama instansi setelah diubah (class method): {User.nama_instansi}')
    print(f'Validasi email pemain1 (static method): {User.validasi_email(pemain1.email)}')
    
    print('\n--- [3] Relasi ASOSIASI (Pelatih - Jadwal - Pendaftaran) ---')
    jadwal_home = pelatih1.buat_jadwal('latihan', '2026-10-20', kuota=2)
    jadwal_away = pelatih2.buat_jadwal('pertandingan', '2026-11-05', kuota=1, lokasi='Suntory Sunbirds Arena (Away)')
    jadwal_home.tampilkan_jadwal()
    print('-')
    jadwal_away.tampilkan_jadwal()
    print(f"\nValidasi format tanggal '2026-10-20' (static method): {Jadwal.validasi_format_tanggal('2026-10-20')}")
    print(f"Validasi format tanggal 'asal-tulis' (static method): {Jadwal.validasi_format_tanggal('asal-tulis')}")
    
    print('\nPemain mendaftar ke sesi:')
    daftar1 = pemain1.daftar_sesi(jadwal_home)
    daftar2 = pemain2.daftar_sesi(jadwal_home)
    daftar3 = pemain3.daftar_sesi(jadwal_home)
    
    print('\nPelatih mengonfirmasi pendaftaran:')
    pelatih1.konfirmasi_pendaftaran(daftar1)
    pelatih1.konfirmasi_pendaftaran(daftar2)
    pelatih1.konfirmasi_pendaftaran(daftar3)
    daftar1.tampilkan()
    print('-')
    daftar3.tampilkan()
    print(f"\nValidasi status 'dikonfirmasi' (static method): {Pendaftaran.validasi_status('dikonfirmasi')}")
    print(f"Validasi status 'expired' (static method): {Pendaftaran.validasi_status('expired')}")
    
    print('\n--- [4] Proses Pembayaran Iuran (2 Objek Pembayaran) ---')
    bayar1 = pemain1.bayar_iuran(daftar1, 15000, 'qris')
    bayar2 = Pembayaran.buat_pembayaran(daftar2, 15000, 'transfer')
    bayar1.tampilkan()
    print('-')
    bayar2.tampilkan()
    print('\nPelatih memverifikasi pembayaran:')
    pelatih1.verifikasi_pembayaran(bayar1)
    bayar1.tampilkan()
    print(f"\nValidasi metode 'transfer' (static method): {Pembayaran.validasi_metode('transfer')}")
    print(f"Validasi metode 'kartu_kredit' (static method): {Pembayaran.validasi_metode('kartu_kredit')}")
    
    print('\n--- [5] Uji Validasi Setter (Property) ---')
    print('\n> Password User (min. 6 karakter)')
    pemain1.password = 'passwordbaru123'
    pemain1.password = '123'
    print(f'Password pemain1 saat ini (lewat getter): {pemain1.password}')
    print('\n> Kuota Jadwal (tidak boleh negatif)')
    jadwal_home.kuota = 8
    jadwal_home.kuota = -3
    print(f'Kuota jadwal_home saat ini (lewat getter): {jadwal_home.kuota}')
    print('\n> Status Pendaftaran (harus sesuai status_valid)')
    daftar2.status = 'menunggu'
    daftar2.status = 'dibatalkan_total'
    print(f'Status daftar2 saat ini (lewat getter): {daftar2.status}')
    print('\n> Jumlah Pembayaran (tidak boleh negatif)')
    bayar2.jumlah = 20000
    bayar2.jumlah = -5000
    print(f'Jumlah bayar2 saat ini (lewat getter): ¥{bayar2.jumlah:,.0f}')
    
    print('\n--- [6] Pemain Membatalkan Pendaftaran ---')
    daftar_away = pemain3.daftar_sesi(jadwal_away)
    daftar_away.tampilkan()
    daftar_away.batalkan()
    daftar1.batalkan()
    
    print('\n--- [7] Relasi AGREGASI (Tim - Pemain) ---')
    tim1 = Tim('Osaka Bluteon Main Squad', 'Hirakata, Osaka')
    tim2 = Tim('Osaka Bluteon Reserve', 'Hirakata, Osaka')
    pelatih1.rekrut_pemain(tim1, pemain1)
    pelatih1.rekrut_pemain(tim1, pemain2)
    tim1.tampilkan_tim()
    tim1.keluarkan_pemain(pemain2)
    tim2.tambah_pemain(pemain2)
    print()
    tim1.tampilkan_tim()
    print('-')
    tim2.tampilkan_tim()
    print("-> Objek 'pemain2' tidak pernah dibuat ulang saat pindah tim, ini ciri AGREGASI (whole-part lemah).")
    
    print('\n--- [8] Relasi KOMPOSISI (Tim - Kas) ---')
    tim1.isi_kas(500000)
    tim1.isi_kas(-50000)
    tim1.cek_kas()
    tim2.cek_kas()
    print('-> Objek Kas disimpan sebagai atribut private (self.__kas) di dalam Tim dan hanya bisa diakses lewat method Tim -> KOMPOSISI.')
    
    print('\n--- Ringkasan Statistik Sistem (Atribut Kelas) ---')
    print(f'Total User (Pelatih+Pemain) : {User.total_user}')
    print(f'Total Jadwal                : {Jadwal.total_jadwal}')
    print(f'Total Pendaftaran           : {Pendaftaran.total_pendaftaran}')
    print(f'Total Pembayaran            : {Pembayaran.total_pembayaran}')
    print(f'Total Tim                   : {Tim.total_tim}')
    print(f'Nama Instansi Saat Ini      : {User.nama_instansi}')