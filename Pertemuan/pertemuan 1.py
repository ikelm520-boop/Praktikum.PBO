# class mobil:
#     def __init__(self, brand, series, warna):
#         self.brand = brand
#         self.series = series
#         self.warna = warna

#     def infomobil(self):
#         print(f"mobil ini memiliki brand {self.brand}")

#     def jual(self):
        

#     def __str__(self):
#         print(f"mobil ini brandnya adalah{self.brand} dengan series {self.series}, warnanya adalah{self.warna} ")


# mobil1 = mobil("lamborgini", "aventador", "merah janda")
# mobil2 = mobil("honda", "freid", "putih")

# mobil1.infomobil()
# mobil2.infomobil()
# mobil1

# print(mobil1)
# print(mobil2)

# class hero:
#     jumlah hero = 0

#     def __init__(self, nama, hp, attacpower, role):
#         self.nama = nama
#         self.hp = hp
#         self.attck = attacpower
#         self.role = role
#         hero.jumlah_hero += 1


# class mahasiswa:
#     universitas = "UNMUL"

#     def __init__(self, nama, role):
#         self.nama = nama
#         self.role = role

# Riva = mahasiswa("Riva", "BPH MBKM Hebas SC MIT")
# print(Riva.universitas)
# sifwah = mahasiswa("sifwah", "media asci koot tgtv")
# print(sifwah.universitas)

# sifwah.universitas = "UNMUL idaman"
# print(sifwah.universitas)

class hero:
    jumlah_hero = 0

    def __init__(self, nama, hp, attackpower, role):
        self.nama = nama
        self.health = hp
        self.attack = attackpower
        self.role = role
        hero.jumlah_hero += 1

    def infohero(self):
        print(f"nama hero ini adalah {self.nama}, memiliki health {self.health}, attack power {self.attack}, dan role {self.role}")

    @classmethod
    def jumlahhero(cls):
        print(f"jumlah hero yang telah dibuat adalah {cls.jumlah_hero}")

    def serang(self, musuh):
        print(f"{self.nama} menyerang {musuh.nama} dengan damage {self.attack}")
        musuh.health -= self.attack
        print(f"health {musuh.nama} sekarang adalah {musuh.health}")

    @classmethod
    def dari_dictionary(cls, data):
        return cls(data["nama"], data["hp"], data["attackpower"], data["role"])

    @staticmethod
    def criticalhit(attackpower):
        return attackpower * 1.5

    def serang(self, musuh, attackpower):
       hit = self.criticalhit(attackpower)
       print(f"{self.nama} menyerang {musuh.nama} dengan damage{hit}")

datahero = {"nama" : "claude", "hp" : 2500, "attackpower" : 170, "role" : "marksman"}
claude = hero.dari_dictionary(datahero)
melissa = hero("melissa", 2500, 133, "marksman")
brody = hero("brody", 3000, 120, "marksman hitam")

claude.infohero()
melissa.infohero()
brody.infohero()
hero.jumlahhero()

melissa.serang(brody, melissa.attack)