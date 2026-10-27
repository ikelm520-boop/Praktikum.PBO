# Sistem Manajemen Tim Voli Osaka Bluteon

## 1. Deskripsi Program

Program ini merupakan sistem sederhana untuk mengelola kegiatan tim voli **Osaka Bluteon Volleyball Club**. Program dibuat menggunakan bahasa pemrograman Python dengan menerapkan konsep **Object-Oriented Programming (OOP)**.

Sistem digunakan untuk mengelola data pengguna, jadwal latihan atau pertandingan, pendaftaran pemain, serta pembayaran iuran. Program juga memiliki validasi data dan menerapkan **encapsulation menggunakan property dan setter**.

Program terdiri dari empat class utama, yaitu:

1. `User`
2. `Jadwal`
3. `Pendaftaran`
4. `Pembayaran`

---

## 2. Tujuan Program

Tujuan dari program ini adalah:

* Mengelola data pelatih dan pemain.
* Membuat dan menampilkan jadwal latihan atau pertandingan.
* Mengatur proses pendaftaran pemain.
* Membatasi jumlah pemain berdasarkan kuota jadwal.
* Mengelola pembayaran iuran pemain.
* Melakukan validasi terhadap data yang dimasukkan.
* Menerapkan konsep OOP seperti class, object, attribute, method, encapsulation, property, class method, dan static method.

---

## 3. Struktur Class

### A. Class `User`

Class `User` digunakan untuk menyimpan data pengguna sistem, baik pelatih maupun pemain.

**Atribut:**

* `nama`
* `email`
* `password`
* `role`
* `no_telepon`
* `id_user`
* `nama_instansi`
* `total_user`

Role yang diperbolehkan adalah `pelatih` dan `pemain`. Email juga divalidasi agar memiliki karakter `@`.

**Method utama:**

* `tampilkan_info()` → menampilkan informasi pengguna.
* `dari_dict()` → membuat objek User dari dictionary.
* `ubah_nama_instansi()` → mengubah nama instansi.
* `validasi_email()` → melakukan validasi email.

Password menggunakan atribut private `__password` sehingga tidak dapat diakses secara langsung dari luar class. Akses password menggunakan `property` dan setter. Password juga harus memiliki minimal 6 karakter.

---

### B. Class `Jadwal`

Class `Jadwal` digunakan untuk mengelola jadwal latihan dan pertandingan.

**Atribut:**

* `id_jadwal`
* `jenis_sesi`
* `tanggal`
* `kuota`
* `lokasi`
* `status`
* `jumlah_pendaftar`
* `total_jadwal`

Jenis sesi yang tersedia adalah:

* `latihan`
* `pertandingan`

Jika lokasi tidak diberikan, sistem akan menggunakan lokasi default **GOR Osaka Bluteon (Home)**.

**Method utama:**

* `tampilkan_jadwal()` → menampilkan informasi jadwal.
* `tambah_pendaftar()` → menambah jumlah pendaftar jika kuota masih tersedia.
* `kurangi_pendaftar()` → mengurangi jumlah pendaftar.
* `dari_dict()` → membuat objek jadwal dari dictionary.
* `validasi_format_tanggal()` → memeriksa format tanggal.

Atribut `kuota` menggunakan property dan setter agar nilai yang diberikan harus berupa angka dan tidak boleh negatif.

---

### C. Class `Pendaftaran`

Class `Pendaftaran` digunakan untuk menghubungkan pemain dengan jadwal yang dipilih.

**Atribut:**

* `id_pendaftaran`
* `pemain`
* `jadwal`
* `waktu_daftar`
* `status`
* `total_pendaftaran`

Status pendaftaran yang tersedia:

* `menunggu`
* `dikonfirmasi`
* `ditolak`

Class ini menerima objek `User` dan `Jadwal` sebagai data pemain dan jadwal.

**Method utama:**

* `konfirmasi()` → mengonfirmasi pendaftaran apabila kuota masih tersedia.
* `batalkan()` → membatalkan pendaftaran.
* `tampilkan()` → menampilkan informasi pendaftaran.
* `buat_pendaftaran()` → membuat pendaftaran untuk pemain.

Jika kuota jadwal sudah penuh, pendaftaran akan otomatis ditolak.

---

### D. Class `Pembayaran`

Class `Pembayaran` digunakan untuk mengelola pembayaran iuran pemain.

**Atribut:**

* `id_pembayaran`
* `pendaftaran`
* `jumlah`
* `metode`
* `status_bayar`
* `total_pembayaran`

Metode pembayaran yang tersedia:

* `cash`
* `transfer`
* `qris`

Status pembayaran:

* `belum lunas`
* `lunas`

**Method utama:**

* `verifikasi()` → mengubah status pembayaran menjadi lunas.
* `tampilkan()` → menampilkan informasi pembayaran.

Atribut `jumlah` dan `status_bayar` menggunakan property dan setter sehingga nilai dapat divalidasi sebelum disimpan.

---

## 4. Hubungan Antar Class

Hubungan antar class dalam program adalah:

```text
User
  │
  │ pemain
  ▼
Pendaftaran ──────► Jadwal
  │
  │ pendaftaran
  ▼
Pembayaran
```

Penjelasannya:

* `User` digunakan sebagai data pemain.
* `Pendaftaran` menyimpan pemain dan jadwal yang dipilih.
* `Jadwal` menentukan jenis kegiatan, tanggal, lokasi, dan kuota.
* `Pembayaran` menggunakan data `Pendaftaran` untuk mencatat pembayaran pemain.

Dengan hubungan tersebut, proses sistem berjalan mulai dari **pemain → memilih jadwal → melakukan pendaftaran → pembayaran**.

---

## 5. Konsep OOP yang Digunakan

### Class dan Object

Program menggunakan beberapa class sebagai cetakan objek. Contohnya:

```python
p1 = User("Yuji Nishida", "nishida@bluteon.jp",
          "yuji123", "pemain", "+81802")
```

Kode tersebut membuat object `p1` dari class `User`.

### Attribute

Attribute digunakan untuk menyimpan data objek, seperti nama, email, role, tanggal, kuota, dan jumlah pembayaran.

### Method

Method digunakan untuk menjalankan fungsi tertentu, seperti:

```python
p1.tampilkan_info()
jadwal_home.tampilkan_jadwal()
daftar1.konfirmasi()
bayar1.verifikasi()
```

### Encapsulation

Encapsulation diterapkan menggunakan atribut private seperti:

```python
self.__password
self.__kuota
self.__status
self.__jumlah
self.__status_bayar
```

Atribut tersebut tidak diakses secara langsung, tetapi melalui property dan setter.

### Property dan Setter

Property digunakan untuk mengontrol akses terhadap atribut tertentu.

Contohnya pada password:

```python
@property
def password(self):
    return "********"
```

Sedangkan setter digunakan untuk melakukan validasi sebelum nilai disimpan. Password yang kurang dari 6 karakter akan ditolak.

### Class Method

Program menggunakan `@classmethod`, contohnya:

```python
User.dari_dict()
Jadwal.dari_dict()
Pendaftaran.buat_pendaftaran()
```

Class method digunakan untuk membuat objek atau menjalankan proses yang berhubungan dengan class.

### Static Method

Static method digunakan untuk validasi yang tidak membutuhkan object tertentu, seperti:

```python
User.validasi_email()
Jadwal.validasi_format_tanggal()
```

---

## 6. Alur Kerja Program

Program dijalankan dengan beberapa tahapan.

### Tahap 1 – Membuat User

Program membuat satu pelatih dan beberapa pemain.

Data pemain juga dapat dibuat menggunakan dictionary melalui method `dari_dict()`.

### Tahap 2 – Membuat Jadwal

Program membuat dua jenis jadwal:

* Latihan di kandang atau Home.
* Pertandingan di luar atau Away.

Jadwal memiliki kuota tertentu.

### Tahap 3 – Pendaftaran

Pemain melakukan pendaftaran terhadap jadwal latihan.

Pelatih kemudian mengonfirmasi pendaftaran. Sistem akan mengecek kuota sebelum menerima pendaftaran.

Pada contoh program, jadwal latihan memiliki kuota 2 pemain tetapi terdapat 3 pendaftar. Oleh karena itu, pendaftar yang melebihi kuota akan ditolak.

### Tahap 4 – Pembayaran

Setelah pendaftaran, sistem membuat pembayaran dengan nominal Rp150.000 menggunakan metode QRIS.

Pembayaran kemudian diverifikasi sehingga status berubah menjadi **LUNAS**.

### Tahap 5 – Pengujian Validasi

Program mencoba memberikan beberapa nilai yang tidak valid, seperti:

* Password kurang dari 6 karakter.
* Kuota jadwal bernilai negatif.
* Jumlah pembayaran bernilai negatif.

Nilai tersebut akan ditolak oleh setter.

### Tahap 6 – Pembatalan

Program juga menguji fitur pembatalan pendaftaran.

Pemain melakukan pendaftaran pada jadwal Away kemudian membatalkan pendaftarannya.

### Tahap 7 – Statistik

Pada bagian akhir, program menampilkan jumlah:

* User terdaftar.
* Jadwal dibuat.
* Pendaftaran.
* Record pembayaran.
* Nama instansi.

Data tersebut menggunakan class attribute seperti `total_user`, `total_jadwal`, `total_pendaftaran`, dan `total_pembayaran`.

---

## 7. Panduan Pengujian

### 7.1 Menjalankan Program

Pastikan Python sudah terinstall.

Kemudian buka terminal pada folder tempat file program berada dan jalankan:

```bash
python nama_file.py
```

Contoh:

```bash
python main.py
```

Program akan menampilkan menu pengujian secara otomatis di terminal.

---

### 7.2 Pengujian Pembuatan User

Program membuat beberapa user, yaitu pelatih dan pemain.

Periksa apakah informasi berikut muncul:

```text
ID User
Nama
Email
Role
No. Telp
Instansi
```

Pengujian ini memastikan class `User` dan method `tampilkan_info()` berjalan dengan benar.

---

### 7.3 Pengujian Kuota Jadwal

Jadwal latihan dibuat dengan kuota:

```text
Kuota = 2
```

Kemudian tiga pemain melakukan pendaftaran.

Hasil yang diharapkan:

```text
Pendaftaran #1 → dikonfirmasi
Pendaftaran #2 → dikonfirmasi
Pendaftaran #3 → ditolak
```

Hal ini membuktikan bahwa sistem dapat membatasi jumlah pendaftar berdasarkan kuota.

---

### 7.4 Pengujian Pembayaran

Program membuat pembayaran:

```text
Jumlah  : Rp150.000
Metode  : QRIS
Status  : BELUM LUNAS
```

Setelah method `verifikasi()` dijalankan, hasil yang diharapkan:

```text
Status Bayar : LUNAS
```

---

### 7.5 Pengujian Encapsulation

Pengujian dilakukan dengan memasukkan data yang tidak valid.

#### Password

```python
p1.password = "123"
```

Hasil yang diharapkan:

```text
[GAGAL] Password 'Yuji Nishida' ditolak: minimal 6 karakter.
```

#### Kuota

```python
jadwal_home.kuota = -10
```

Hasil yang diharapkan:

```text
[GAGAL] Kuota jadwal 'latihan' ditolak: harus angka >= 0.
```

#### Jumlah Pembayaran

```python
bayar1.jumlah = -50000
```

Hasil yang diharapkan:

```text
[GAGAL] Jumlah pembayaran ditolak: tidak boleh negatif.
```

Ketiga pengujian tersebut menunjukkan bahwa setter berhasil melakukan validasi terhadap data.

---

### 7.6 Pengujian Pembatalan Pendaftaran

Pemain melakukan pendaftaran pada jadwal Away kemudian membatalkan pendaftaran.

Hasil yang diharapkan adalah status pendaftaran berubah menjadi:

```text
DITOLAK
```

dengan informasi bahwa pendaftaran dibatalkan oleh pemain.

---

## 8. Contoh Output

Secara umum program akan menghasilkan output seperti:

```text
==================================================
 SISTEM MANAJEMEN TIM VOLI OSAKA BLUTEON
==================================================

--- [1] Membuat Objek User (Data Asli) ---

ID User    : 1
Nama       : Laurent Tillie
Email      : tillie@bluteon.jp
Role       : PELATIH
No. Telp   : +81801
Instansi   : Osaka Bluteon Volleyball Club
```

Selanjutnya program menampilkan jadwal, proses pendaftaran, pembayaran, pengujian validasi, pembatalan, dan statistik sistem.

---

## 9. Kesimpulan

Program **Sistem Manajemen Tim Voli Osaka Bluteon** merupakan program berbasis Python yang menerapkan konsep Object-Oriented Programming. Program memiliki empat class utama, yaitu `User`, `Jadwal`, `Pendaftaran`, dan `Pembayaran`.
Program tidak hanya mengimplementasikan class dan object, tetapi juga menggunakan attribute, method, class method, static method, encapsulation, property, dan setter. Selain itu, terdapat validasi untuk memastikan data yang dimasukkan sesuai dengan aturan sistem.
Melalui pengujian yang dilakukan, program dapat menangani proses pembuatan user, pengelolaan jadwal, pendaftaran pemain berdasarkan kuota, pembayaran, pembatalan pendaftaran, serta penolakan data yang tidak valid.
