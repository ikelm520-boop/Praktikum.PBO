# # induk
# class hero:
#     def __init__(self, nama, hp, attack):
#         self.nama = nama
#         self.hp = hp
#         self.attack = attack

#     def hitung_damage(self):
#         return 0

#     def ultimate(self):
#         return f"{self.nama} belum punya ultimate"
# #anak
# class tank(hero):
#     def hitung_damage(self):
#         return self.attack * 1.2
    
#     def ultimate(self):
#         return f"{self.nama} mengeluarkan implusion"

# class mage(hero):
#     def hitung_damage(self):
#         return self.attack * 1.5
    
#     def ultimate(self):
#         return f"{self.nama} mengeluarkan magis"

# tim = [
#     hero('Badeng', 1000, 100),
#     tank('Asoy Merah', 1500, 50),
#     mage('Meilonie', 1500, 100) 
# ]

# for hero in tim:
#     dmg = hero.hitung_damage()
#     print(f"{hero.nama}: {dmg:,.0f} damage")
#     print(f'{hero.ultimate()}')

# class Penyihir: 
#     def __init__(self, nama): 
#         self.nama = nama 
#     def serang(self): 
#         print(f'{self.nama} melempar bola api!') 

# class Menara: 
#     def serang(self):  
#         print('Menara menembakkan laser!')  
        
# class Creep: 
#     def serang(self): 
#         print('Creep memukul pelan.') 
        
# class Batu: 
#     pass 

# def mulai_pertempuran(penyerang_list): 
#     for p in penyerang_list: 
#         p.serang() 


# mulai_pertempuran([ 
#     Penyihir('Eudora'), Menara(), Creep(), ]) 

# try: 
#     mulai_pertempuran([Batu()]) 
# except AttributeError as e: 
#     print(f'Error: {e}')

# from abc import ABC, abstractmethod

# class HeroBase(ABC):
#     def SeranganDasar(self):
#         pass

#     @abstractmethod
#     def GunakanUltimate(self):
#         pass

# class Layla(HeroBase):
#     def __init__(self, level):
#         self.level = level

#     def SeranganDasar(self):
#         print("Layla menembakkan Machine Gun")

#     def GunakanUltimate(self):
#         print(f"Layla level {self.level} mengunakan Skill ultimete nya")

# class HeroBug(HeroBase):
#     def SeranganDasar(self):
#         pass

# Hero_1 = Layla(15)
# Hero_1.GunakanUltimate()

# try:
#     Hero_2 = HeroBug()
#     Hero_2.GunakanUltimate()

# class statushero:
#     def __init__(self, nama, hp, attack):
#         self.nama = nama
#         self.hp = hp
#         self.attack = attack
        
#     def __add__(self, itemstats):
#         hp_baru = self.hp + itemstats.hp
#         attack_baru = self.attack + itemstats.attack
#         return statushero(self.nama, hp_baru, attack_baru)
        
#     def __gt__(self, hero_lain):
#         return self.hp > hero_lain.hp
        
#     def __str__(self):
#         return f"{self.nama}, {self.hp}, {self.attack}"

# # Inisialisasi Hero dan Item sesuai gambar baru
# chou_awal = statushero("chou", 3000, 150)
# bod = statushero("item1", 0, 150)
# nod = statushero("item2", 150, 0) # Menambahkan item kedua

# # Chou membeli dua item sekaligus (BOD + NOD)
# chou_jadi = chou_awal + bod + nod

# # Inisialisasi hero musuh (Aldous)
# aldous = statushero("aldous", 4000, 200)

# # Menampilkan status aldous
# print(aldous) 

# # Membandingkan apakah HP Chou setelah beli item lebih besar dari HP Aldous
# print(f"apakah chou lebih tebal dari aldous? {chou_jadi > aldous}")

class KalkulatorBunga:
    def hitung(self, saldo, persen=2, bulan=1):
        # Satu method, beberapa "versi" pemanggilan
        return saldo * (persen / 100) * (bulan / 12)

    def total_setoran(self, *jumlah):
        # Menerima setoran sebanyak apapun
        return sum(jumlah)

kalkulator = KalkulatorBunga()
print(f"{kalkulator.hitung(1_000_000):,.2f}") 
print(f"{kalkulator.hitung(1_000_000, 6):,.2f}")
print(f"{kalkulator.hitung(1_000_000, 6, 12):,.2f}") 
print(kalkulator.total_setoran(500_000)) #
print(kalkulator.total_setoran(500_000, 250_000, 100_000)) 