# Osaka Bluteon Volleyball Club - Sistem Manajemen 

Proyek ini adalah implementasi sistem manajemen berbasis Object-Oriented Programming (OOP) dalam bahasa Python untuk **Osaka Bluteon Volleyball Club** (sebuah klub bola voli profesional peserta SV.League Jepang).

Sistem ini dirancang untuk mendemonstrasikan penerapan konsep-konsep inti OOP secara mendalam, termasuk enkapsulasi, pewarisan (*inheritance*), polimorfisme, *class methods*, *static methods*, serta relasi antar objek (Asosiasi, Agregasi, dan Komposisi).

## Fitur Utama & Konsep OOP yang Diterapkan

1. **Inheritance & Polymorphism (`User`, `Pelatih`, `Pemain`)**:

   * Kelas `User` bertindak sebagai *parent class* yang mencakup atribut dasar seperti nama, email, nomor telepon, password, dan *role*.

   * Kelas `Pelatih` dan `Pemain` mewarisi sifat dari `User` (*subclass*).

   * Menerapkan *method overriding* pada fungsi `tampilkan_info()` di setiap *subclass* untuk menampilkan informasi spesifik masing-masing peran.

2. **Encapsulation & Property Getters/Setters**:

   * Validasi data ketat menggunakan `@property` dan setter (misalnya pada validasi panjang minimal password, kuota jadwal yang tidak boleh negatif, status pendaftaran yang valid, dan jumlah pembayaran).

3. **Class Methods & Static Methods**:

   * **Class Method**: Digunakan untuk memanipulasi data tingkat kelas (seperti mengubah nama instansi klub via `User.ubah_nama_instansi()`) atau memuat data objek dari kamus (*factory method* `dari_dict()`).

   * **Static Method**: Berfungsi sebagai fungsi utilitas independen yang tidak bergantung pada instansiasi objek, seperti validasi format email, validasi tanggal, dan validasi metode pembayaran.

4. **Relasi Antar Objek**:

   * **Asosiasi**: Hubungan antara `Pelatih` yang membuat `Jadwal`, serta `Pemain` yang melakukan `Pendaftaran`.

   * **Agregasi (Whole-Part Lemah)**: Hubungan antara `Tim` dan `Pemain`. Pemain dapat dimasukkan atau dikeluarkan dari tim tanpa membuat objek pemain baru atau menghapus objek pemain tersebut dari sistem.

   * **Komposisi (Whole-Part Kuat)**: Hubungan antara `Tim` dan `Kas`. Objek `Kas` dibuat di dalam inisialisasi kelas `Tim` (`self.__kas`) dan bersifat privat serta bergantung sepenuhnya pada keberadaan objek `Tim`.

## Entitas dan Anggota Klub (Data Nyata Osaka Bluteon)

Sistem ini menggunakan data nyata dari skuad klub Osaka Bluteon (sebelumnya dikenal sebagai Panasonic Panthers):

* **Pelatih Kepala:** Laurent Tillie (Spesialisasi: Head Coach & Taktik)

* **Asisten Pelatih:** Toshiaki Kawai

* **Pemain:**

  * Yuji Nishida (Opposite, #11)

  * Thomas Jaeschke (Outside Hitter, #8)

  * Akihiro Yamauchi (Middle Blocker, #13)

## Struktur Berkas Proyek

* `main.py` (atau file utama kode OOP): Berisi seluruh definisi kelas (`User`, `Pelatih`, `Pemain`, `Jadwal`, `Pendaftaran`, `Pembayaran`, `Kas`, `Tim`) beserta blok pengujian skenario interaksi sistem di bagian `if __name__ == '__main__':`.

## Cara Menjalankan Program

1. Pastikan Anda telah menginstal **Python** (versi 3.x direkomendasikan) di komputer Anda.

2. Salin kode program Python ke dalam file lokal, misalnya `app.py`.

3. Buka terminal atau command prompt pada direktori file tersebut.

4. Jalankan perintah berikut:

   ```
   python app.py
   
   ```

## Contoh Alur Pengujian dalam Program

* Pembuatan objek pengguna (pelatih & pemain) baik secara langsung maupun melalui fungsi `.dari_dict()`.

* Pengujian polimorfisme untuk menampilkan profil lengkap masing-masing anggota.

* Pelatih membuat sesi latihan/pertandingan, dilanjutkan dengan pendaftaran pemain dan konfirmasi kuota oleh pelatih.

* Simulasi pembayaran iuran menggunakan metode pembayaran yang valid (`qris`, `transfer`, `cash`) dan verifikasi pembayarannya.

* Pengujian error handling pada *setter* (misalnya memasukkan kuota negatif atau password kurang dari 6 karakter).

* Simulasi pemindahan pemain antar tim (Agregasi) dan manajemen pengelolaan saldo kas tim (Komposisi).