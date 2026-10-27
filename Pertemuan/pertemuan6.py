# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def serang(self, target): # tugas 1: pertarungan
#         target.health -= 10

#     def tampilkan_status(self): # tugas 2: tampilan
#         print(f"{self.name} | HP {self.health}")

#     def simpan(self, nama_file): # tugas 3: penyimpanan
#         with open(nama_file, "a") as f:
#             f.write(f"{self.name},{self.health}\n")

# #single responsibility principle
# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def serang(self, target):
#         target.health -= 10

# class Tampilkanhero:
#     def menampilkanHero(self, hero):
#         print(f"{hero.name} | HP {hero.health}")

# class Penyimpananhero:
#     def menyimpanHero(self, hero, nama_file):
#         with open(nama_file, "a") as f:
#             f.write(f"{hero.name},{hero.health}\n")

# esme = Hero("Esmeralda", 100)
# Hero("Benedetta", 120).serang(esme)
# tampilkanHero = Tampilkanhero()
# tampilkanHero.menampilkanHero(esme)
# penyimpananHero = Penyimpananhero()
# penyimpananHero.menyimpanHero(esme, "hero_data.txt")

# class Hero:
#     def __init__(self, attack):
#         self.attack = attack

#     def hitung_damage(self):
#         return self.attack

# class Fighter(Hero):
#     def hitung_damage(self):
#         return self.attack + 5
    
# class Mage(Hero):
#     def hitung_damage(self):
#         return self.attack + 3
# class Assassin(Hero):
#     def hitung_damage(self):
#         return self.attack + 4

# print(Fighter(10).hitung_damage())
# print(Mage(5).hitung_damage())

# class Unit:
#     pass
#     print("Unit bergerak")

# class Minion(Unit):
#     pass

# class Turret(Unit):
#     def bergerak(self): # melanggar janji parent
#         raise Exception("Turret tidak bisa bergerak!")

#     def maju(unit: Unit):

# unit.bergerak()
# maju(Minion())
# maju(Turret())

# from abc import ABC, abstractmethod

# class BisaMenyerang(ABC):
#     @abstractmethod
#     def serang(self):
#         pass

# class BisaHealing():
#     @abstractmethod
#     def heal(self):
#         pass

# class Fighter(BisaMenyerang, BisaHealing):
#     def __init__(self):
#         self.name = "Fighter"

#     def serang(self):
#         print("Fighter menyerang")

#     def heal(self): # dipaksa ada, padahal tidak bisa
#         raise NotImplementedError("Fighter tidak bisa heal")

# Fighter().serang()
# Fighter().heal()

