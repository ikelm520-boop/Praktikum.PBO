# Sistem Manajemen Osaka Bluteon Volleyball Club

Program OOP Python untuk mengelola klub voli: pelatih dan pemain (`User`), jadwal latihan/pertandingan, pendaftaran sesi, pembayaran iuran, tim, dan kas tim. Program ini menerapkan **Abstraksi** (Abstract Base Class) dan **Polimorfisme**, dengan konsep inheritance dari posttest sebelumnya tetap dipakai (`super().__init__()`, atribut unik subclass, atribut protected/private).

Cara menjalankan:

```bash
python main.py
```

## 1. Class Diagram

![Class Diagram](classDiagram.png)

Diagram dibuat dengan Graphviz (`class_diagram.dot`) lalu diekspor ke `class_diagram.png`.

### Penjelasan Relasi

- **Asosiasi** (garis dengan panah terbuka). Contohnya `Jadwal` → `Pelatih` (atribut `pelatih_penanggungjawab`), `Pendaftaran` → `Pemain` dan `Jadwal`, serta `Pembayaran` → `Pendaftaran`. Kelas-kelas ini hanya saling merujuk lewat atribut dan tidak saling memiliki; masing-masing objek dibuat dan hidup sendiri-sendiri.
- **Agregasi** (belah ketupat kosong): `Tim` ◇— `Pemain`, lewat atribut `Tim.daftar_pemain`. Objek `Pemain` dibuat di luar Tim lalu dimasukkan lewat `tambah_pemain()`. Dipilih agregasi karena Pemain tetap ada walaupun keluar dari Tim. Di output, `pemain2` dikeluarkan dari `tim1` lalu dimasukkan ke `tim2` tanpa dibuat ulang.
- **Komposisi** (belah ketupat penuh): `Tim` ◆— `Kas`, lewat `self.__kas = Kas(nama_tim)` di `Tim.__init__()`. Objek Kas dibuat di dalam Tim, bersifat private, dan hanya bisa diakses lewat method Tim (`isi_kas()`, `cek_kas()`). Dipilih komposisi karena kas tim tidak punya arti tanpa timnya, sehingga siklus hidupnya mengikuti Tim.

Ringkasnya, agregasi dipilih bila bagian dibuat di luar dan bisa hidup mandiri (Pemain), sedangkan komposisi dipilih bila bagian dibuat dan dimiliki penuh oleh keseluruhannya (Kas).

## 2. Abstraksi

- **Abstract class:** `User(ABC)`.
- **Abstract method (2 buah):** `deskripsi_peran()` dan `aksi_utama()`, keduanya `@abstractmethod`.
- **Subclass yang mengimplementasikan keduanya:** `Pelatih` dan `Pemain`.
- **Method konkret bersama:** `jalankan_rutinitas()` di `User`, dipakai kedua subclass tanpa di-override. Method ini memanggil `deskripsi_peran()` dan `aksi_utama()` milik masing-masing subclass. `tampilkan_info()` juga method konkret di `User` yang diperluas subclass lewat `super()`.
- **Inheritance:** `Pelatih` dan `Pemain` memakai `super().__init__(...)` dengan atribut unik (`spesialisasi`; `posisi` dan `nomor_punggung`).
- **Enkapsulasi:** `_id_user` (protected); `__password`, `__kuota`, `__status`, `__jumlah`, `__status_bayar`, `__kas` (private) dengan getter/setter `@property`.
- **Bukti abstract class tidak bisa diinstansiasi:** `User(...)` dibungkus `try-except TypeError` di bagian `[0]` program. Hasilnya ada di screenshot output.

## 3. Polimorfisme

| Konsep | Penerapan |
|---|---|
| Polimorfisme via pewarisan | `tampilkan_info()`, `deskripsi_peran()`, dan `aksi_utama()` di-override `Pelatih` dan `Pemain` dengan perilaku berbeda. Dipanggil dalam satu loop `for u in semua_user` (bagian `[2]`) yang berisi objek Pelatih dan Pemain. |
| Duck typing | `Pendaftaran` dan `Pembayaran` tidak berhubungan lewat pewarisan, tetapi sama-sama punya method `tampilkan()`. Keduanya dipanggil lewat fungsi yang sama, `cetak_dokumen(dokumen)` (bagian `[9]`). |
| Operator overloading | `User.__str__`, `Pemain.__lt__` (urut nomor punggung), `Pembayaran.__add__` (total dua pembayaran), `Tim.__len__` (jumlah pemain). Hasilnya di bagian `[10]`. |
| Tanpa anti-pattern | Perilaku tiap objek ditentukan oleh method-nya sendiri, tidak ada rantai `if/elif` yang mengecek `type()` atau string jenis. Ada pengecekan `isinstance` tunggal di `Pendaftaran.buat_pendaftaran()` dan `Tim.tambah_pemain()`, tetapi itu hanya validasi masukan, bukan pembeda perilaku. |

## SS OUTPUT

Output lengkap `python main.py` dibagi menjadi beberapa gambar. Bukti abstract class tidak bisa diinstansiasi ada di gambar pertama (bagian `[0]`).

![Output 1](1.png)
![Output 2](2.png)


## Struktur File

```
main.py            # kode program
class_diagram.dot  # sumber diagram (Graphviz)
class_diagram.png  # class diagram
output_1..7.png    # screenshot output
output.txt         # output teks lengkap
README.md
```