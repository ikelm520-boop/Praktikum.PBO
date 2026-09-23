# class MesinATM:
#     def __init__(self, id_atm, lokasi, saldo_kas):
#         self.id_atm = id_atm
#         self.lokasi = lokasi
#         self.saldo_kas = saldo_kas

#     def verifikasi_pin(self, nasabah, pin_input):
#         return nasabah.cek_pin(pin_input)

#     def proses_penarikan(self, nasabah, jumlah):
#         if jumlah <= 0:
#             print("❌ Jumlah penarikan harus lebih dari Rp0.")
#             return False
        
#         if jumlah > self.saldo_kas:
#             print(f"❌ [ATM {self.id_atm}] Gagal: Saldo kas mesin ATM tidak mencukupi.")
#             return False
            
#         if jumlah > nasabah.saldo_rekening:
#             print(f"❌ [ATM {self.id_atm}] Gagal: Saldo rekening Anda tidak mencukupi.")
#             return False

#         # Proses pemotongan jika semua validasi lolos
#         self.saldo_kas -= jumlah
#         nasabah.saldo_rekening -= jumlah
#         print(f"✅ [ATM {self.id_atm}] Penarikan Rp{jumlah:,} berhasil!")
#         return True

#     def proses_setoran(self, nasabah, jumlah):
#         if jumlah <= 0:
#             print("❌ Jumlah setoran harus lebih dari Rp0.")
#             return False
            
#         # Proses penambahan saldo
#         self.saldo_kas += jumlah
#         nasabah.saldo_rekening += jumlah
#         print(f"✅ [ATM {self.id_atm}] Setor tunai Rp{jumlah:,} berhasil!")
#         return True


# class Nasabah:
#     def __init__(self, nama, nomor_rekening, pin, saldo_rekening):
#         self.nama = nama
#         self.nomor_rekening = nomor_rekening
#         self.__pin = pin  # Private attribute untuk keamanan PIN
#         self.saldo_rekening = saldo_rekening

#     def cek_pin(self, pin_input):
#         return self.__pin == pin_input


# # --- Fungsi Menu Utama Simulasi ---
# def jalankan_atm(atm_obj, daftar_nasabah):
#     print(f"=== SELAMAT DATANG DI {atm_obj.id_atm} ===")
#     print(f"Lokasi: {atm_obj.lokasi}\n")
    
#     # 1. Input Nomor Rekening
#     norek_input = input("Masukkan Nomor Rekening Anda: ").strip()
#     nasabah_aktif = daftar_nasabah.get(norek_input)
    
#     if not nasabah_aktif:
#         print("❌ Nomor rekening tidak terdaftar. Sesi diakhiri.")
#         return

#     # 2. Input PIN (Maksimal 3 kali percobaan)
#     percobaan = 3
#     autentikasi_berhasil = False
    
#     while percobaan > 0:
#         pin_input = input(f"Masukkan PIN Anda (Sisa percobaan {percobaan}): ")
#         if atm_obj.verifikasi_pin(nasabah_aktif, pin_input):
#             autentikasi_berhasil = True
#             break
#         else:
#             print("❌ PIN Salah!")
#             percobaan -= 1
            
#     if not autentikasi_berhasil:
#         print("❌ Anda salah memasukkan PIN 3 kali. Kartu Anda diblokir!")
#         return

#     # 3. Menu Transaksi Setelah Login Berhasil
#     print(f"\nSelamat Datang, {nasabah_aktif.nama}!")
#     while True:
#         print("\n--- MENU ATM ---")
#         print("1. Cek Saldo")
#         print("2. Tarik Tunai")
#         print("3. Setor Tunai")
#         print("4. Keluar (Ambil Kartu)")
        
#         pilihan = input("Pilih menu (1-4): ").strip()
        
#         if pilihan == "1":
#             print(f"💰 Saldo Rekening Anda: Rp{nasabah_aktif.saldo_rekening:,}")
            
#         elif pilihan == "2":
#             try:
#                 nominal = int(input("Masukkan nominal penarikan: Rp"))
#                 atm_obj.proses_penarikan(nasabah_aktif, nominal)
#             except ValueError:
#                 print("❌ Input harus berupa angka penuh.")
                
#         elif pilihan == "3":
#             try:
#                 nominal = int(input("Masukkan nominal setoran: Rp"))
#                 atm_obj.proses_setoran(nasabah_aktif, nominal)
#             except ValueError:
#                 print("❌ Input harus berupa angka penuh.")
                
#         elif pilihan == "4":
#             print("👋 Terima kasih telah menggunakan layanan kami. Silakan ambil kartu Anda.")
#             break
#         else:
#             print("❌ Pilihan menu tidak valid.")


# # --- Inisialisasi Data / Database Sederhana ---
# atm_sudirman = MesinATM("ATM-BCA-01", "Kantor Cabang Sudirman", 50_000_000)

# # Menggunakan dictionary untuk mencari nasabah berdasarkan nomor rekening dengan cepat
# database_nasabah = {
#     "101-220-334": Nasabah("Budi Santoso", "101-220-334", "123456", 2_000_000),
#     "101-445-889": Nasabah("Siti Rahma", "101-445-889", "654321", 500_000)
# }

# # Jalankan Program
# if __name__ == "__main__":
#     jalankan_atm(atm_sudirman, database_nasabah)


class CatatanTransaksi:
    """Objek ini tidak memiliki arti mandiri tanpa rekening tempat mutasi terjadi."""
    
    def __init__(self, id_transaksi, tipe, nominal, keterangan):
        self.id_transaksi = id_transaksi
        self.tipe = tipe
        self.nominal = nominal
        self.keterangan = keterangan

    def __str__(self):
        simbol = "+" if self.tipe == "KREDIT" else "-"
        return f"[{self.id_transaksi}] {self.tipe:<6} {simbol}Rp{self.nominal:,} | Ket: {self.keterangan}"


class Rekening:
    """
    Rekening terdiri dari CatatanTransaksi.
    Catatan dibuat di dalam rekening dan musnah bersama rekening tersebut.
    """
    
    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal
        self._riwayat = []
        if saldo_awal > 0:
            self._buat_catatan("KREDIT", saldo_awal, "Setoran awal pembukaan rekening")

    def _buat_catatan(self, tipe, nominal, keterangan):
        """Objek bagian dibuat langsung di dalam induk."""
        id_baru = f"TRX-{len(self._riwayat) + 1:04d}"
        catatan = CatatanTransaksi(id_baru, tipe, nominal, keterangan)
        self._riwayat.append(catatan)

    def setor(self, nominal, keterangan="Setor tunai"):
        self.saldo += nominal
        self._buat_catatan("KREDIT", nominal, keterangan)
        print(f" Setoran Rp{nominal:,} berhasil dicatat.")

    def tarik(self, nominal, keterangan="Tarik tunai"):
        if nominal <= self.saldo:
            self.saldo -= nominal
            self._buat_catatan("DEBET", nominal, keterangan)
            print(f" Penarikan Rp{nominal:,} berhasil dicatat.")
        else:
            print(" Saldo tidak mencukupi untuk transaksi.")

    def cetak_rekening_koran(self):
        print(f"\n Rekening Koran: {self.nomor_rekening} an {self.nama_pemilik}")
        print(f" Saldo Akhir: Rp{self.saldo:,}")
        print(" Riwayat Mutasi Transaksi:")
        for trx in self._riwayat:
            print(f" {trx}")


# Pembuatan objek induk secara otomatis merakit bagian-bagian internalnya
tabungan = Rekening("554-900-112", "Rina Marlina", 2000000)
tabungan.setor(500000, "Transfer masuk dari klien")
tabungan.tarik(300000, "Pembayaran listrik")
tabungan.cetak_rekening_koran()

# Bukti komposisi: Ketika rekening ditutup dan dihapus
del tabungan
# Riwayat CatatanTransaksi ikut terhapus karena berada di dalam instance rekening tersebut.