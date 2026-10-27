
data_konser = [
    (1, "LANY - Jakarta", "Jakarta", 850000, 100),
    (2, "LANY - Surabaya", "Surabaya", 750000, 80),
    (3, "LANY - Bali", "Bali", 900000, 60)
]

data_user = [
    ("admin", "admin123", "admin")
]

data_transaksi = []

while True:
    print("\n=== SISTEM PENJUALAN TIKET KONSER LANY ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        username = input("Username: ")
        password = input("Password: ")

        status_login = False
        peran = ""

        for user in data_user:
            if user[0] == username and user[1] == password:
                status_login = True
                peran = user[2]

        if status_login:
            print("\nLogin berhasil!")

            if peran == "admin":
                while True:
                    print("\n=== MENU ADMIN ===")
                    print("1. Lihat Data Konser")
                    print("2. Tambah Konser")
                    print("3. Ubah Data Konser")
                    print("4. Hapus Konser")
                    print("5. Logout")

                    menu_admin = input("Pilih menu: ")

                    if menu_admin == "1":
                        print("\n=== DAFTAR KONSER ===")

                        for konser in data_konser:
                            print(
                                "ID:", konser[0],
                                "| Nama:", konser[1],
                                "| Kota:", konser[2],
                                "| Harga: Rp", konser[3],
                                "| Stok:", konser[4]
                            )

                    elif menu_admin == "2":
                        id_konser = len(data_konser) + 1
                        nama = input("Nama konser: ")
                        kota = input("Kota konser: ")
                        harga = input("Harga tiket: ")
                        stok = input("Jumlah tiket: ")

                        if harga.isdigit() and stok.isdigit():
                            data_konser.append(
                                (id_konser, nama, kota, int(harga), int(stok))
                            )
                            print("Konser berhasil ditambahkan.")
                        else:
                            print("Harga dan stok harus berupa angka.")

                    elif menu_admin == "3":
                        print("\n=== DAFTAR KONSER ===")

                        for konser in data_konser:
                            print(
                                konser[0], "-", konser[1],
                                "| Harga:", konser[3],
                                "| Stok:", konser[4]
                            )

                        id_edit = input("Masukkan ID konser yang diubah: ")

                        if id_edit.isdigit():
                            ditemukan = False

                            for i in range(len(data_konser)):
                                if data_konser[i][0] == int(id_edit):
                                    nama_baru = input("Nama konser baru: ")
                                    kota_baru = input("Kota baru: ")
                                    harga_baru = input("Harga baru: ")
                                    stok_baru = input("Stok baru: ")

                                    if harga_baru.isdigit() and stok_baru.isdigit():
                                        data_konser[i] = (
                                            data_konser[i][0],
                                            nama_baru,
                                            kota_baru,
                                            int(harga_baru),
                                            int(stok_baru)
                                        )
                                        print("Data konser berhasil diubah.")
                                    else:
                                        print("Harga dan stok harus berupa angka.")

                                    ditemukan = True

                            if not ditemukan:
                                print("ID konser tidak ditemukan.")
                        else:
                            print("ID harus berupa angka.")

                    elif menu_admin == "4":
                        print("\n=== DAFTAR KONSER ===")

                        for konser in data_konser:
                            print(konser[0], "-", konser[1])

                        id_hapus = input("Masukkan ID konser yang dihapus: ")

                        if id_hapus.isdigit():
                            ditemukan = False

                            for i in range(len(data_konser)):
                                if data_konser[i][0] == int(id_hapus):
                                    data_konser.pop(i)
                                    print("Konser berhasil dihapus.")
                                    ditemukan = True
                                    break

                            if not ditemukan:
                                print("ID konser tidak ditemukan.")
                        else:
                            print("ID harus berupa angka.")

                    elif menu_admin == "5":
                        print("Logout berhasil.")
                        break

                    else:
                        print("Pilihan tidak tersedia.")

            else:
                while True:
                    print("\n=== MENU PENGGUNA ===")
                    print("1. Lihat Daftar Konser")
                    print("2. Beli Tiket")
                    print("3. Riwayat Transaksi")
                    print("4. Logout")

                    menu_user = input("Pilih menu: ")

                    if menu_user == "1":
                        print("\n=== DAFTAR KONSER ===")

                        for konser in data_konser:
                            print(
                                "ID:", konser[0],
                                "| Nama:", konser[1],
                                "| Kota:", konser[2],
                                "| Harga: Rp", konser[3],
                                "| Stok:", konser[4]
                            )

                    elif menu_user == "2":
                        print("\n=== DAFTAR KONSER ===")

                        for konser in data_konser:
                            print(
                                "ID:", konser[0],
                                "|", konser[1],
                                "| Harga: Rp", konser[3],
                                "| Stok:", konser[4]
                            )

                        id_beli = input("Masukkan ID konser: ")

                        if id_beli.isdigit():
                            ditemukan = False

                            for i in range(len(data_konser)):
                                if data_konser[i][0] == int(id_beli):
                                    ditemukan = True

                                    if data_konser[i][4] > 0:
                                        jumlah = input("Jumlah tiket: ")

                                        if jumlah.isdigit() and int(jumlah) > 0:
                                            if int(jumlah) <= data_konser[i][4]:
                                                total = int(jumlah) * data_konser[i][3]

                                                print("Nama konser:", data_konser[i][1])
                                                print("Jumlah tiket:", int(jumlah))
                                                print("Total pembayaran: Rp", total)

                                                konfirmasi = input(
                                                    "Konfirmasi pembelian? (y/n): "
                                                )

                                                if konfirmasi.lower() == "y":
                                                    stok_baru = (
                                                        data_konser[i][4] - int(jumlah)
                                                    )

                                                    data_konser[i] = (
                                                        data_konser[i][0],
                                                        data_konser[i][1],
                                                        data_konser[i][2],
                                                        data_konser[i][3],
                                                        stok_baru
                                                    )

                                                    data_transaksi.append(
                                                        (
                                                            username,
                                                            data_konser[i][1],
                                                            int(jumlah),
                                                            total
                                                        )
                                                    )

                                                    print("Pembelian berhasil.")
                                                else:
                                                    print("Pembelian dibatalkan.")
                                            else:
                                                print("Stok tiket tidak mencukupi.")
                                        else:
                                            print("Jumlah tiket harus berupa angka positif.")
                                    else:
                                        print("Tiket sudah habis.")

                            if not ditemukan:
                                print("ID konser tidak ditemukan.")
                        else:
                            print("ID harus berupa angka.")

                    elif menu_user == "3":
                        print("\n=== RIWAYAT TRANSAKSI ===")
                        ada_transaksi = False

                        for transaksi in data_transaksi:
                            if transaksi[0] == username:
                                print(
                                    "Konser:", transaksi[1],
                                    "| Jumlah:", transaksi[2],
                                    "| Total: Rp", transaksi[3]
                                )
                                ada_transaksi = True

                        if not ada_transaksi:
                            print("Belum ada transaksi.")

                    elif menu_user == "4":
                        print("Logout berhasil.")
                        break

                    else:
                        print("Pilihan tidak tersedia.")

        else:
            print("Username atau password salah.")

    elif pilihan == "2":
        username_baru = input("Buat username: ")
        password_baru = input("Buat password: ")

        username_tersedia = True

        for user in data_user:
            if user[0] == username_baru:
                username_tersedia = False

        if username_tersedia and username_baru != "" and password_baru != "":
            data_user.append((username_baru, password_baru, "user"))
            print("Registrasi berhasil. Silakan login.")
        else:
            print("Username sudah digunakan atau data masih kosong.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program.")
        break

    else:
        print("Pilihan tidak tersedia.")
