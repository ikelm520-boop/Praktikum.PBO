# class RekeningBank():
#     def __init__(self, pemilik, saldo, norek):
#         self._pemilik = pemilik
#         self._saldo = saldo
#         self._norek = norek

#     def get_saldo(self):
#         return self._saldo

#     def set_saldo(self, saldo):
#         if saldo >= 0:
#             self._saldo = saldo
#         else:
#             print("Saldo tidak valid")

# rekening = RekeningBank("Budi", 100000, "12345")
# rekening.set_saldo(-500000) # akan menampilkan pesan kesalahan
# print(rekening.get_saldo()) # 100000, data tetap valid

# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.pemilik = pemilik
#         self.__saldo = saldo

#     def get_saldo(self):
#         return self.__saldo

#     def set_saldo(self, saldo_baru):
#         if saldo_baru < 0:
#             print("Saldo tidak boleh negatif.")
#         else:
#             self.__saldo = saldo_baru

# rekening = RekeningBank("Budi", 100000)
# print(rekening.get_saldo())
# rekening.set_saldo(-500) # ditolak oleh validasi
# rekening.set_saldo(200000) # diterima
# print(rekening.get_saldo())

    # class RekeningBank:
    #     def __init__(self, pemilik, saldo):
    #         self.pemilik = pemilik
    #         self.__saldo = saldo

    #     @property
    #     def saldo(self):
    #         """Getter -- dipanggil seperti atribut biasa, tanpa tanda
    #     kurung."""
    #         return self.__saldo

    #     @saldo.setter
    #     def saldo(self, saldo_baru):
    #         """Setter -- dijalankan otomatis saat ada assignment ke
    #             rekening.saldo"""
    #         if saldo_baru < 0:
    #             raise ValueError("Saldo tidak boleh negatif.")
    #         self.__saldo = saldo_baru

    # rekening = RekeningBank("Budi", 100000)
    # print(rekening.saldo) # dipanggil seperti atribut, bukan method
    # rekening.saldo = 250000 # otomatis lewat setter dengan validasi
    # print(rekening.saldo)