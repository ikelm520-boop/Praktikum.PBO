class hero:
    def __init__(self, name, health, attack, armor, mana=50):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.mana = mana

    def __str__(self):
        return f"nama hero: {self.name}, health: {self.health}, attack: {self.attack}, armor: {self.armor}, mana: {self.mana}"

    class mmaksman(hero):
        def __init__(self, name, health, attack, armor, mana=50):
            super().__init__(name, health, attack, armor, mana)
            self.range = 10

        def __str__(self):
            return f"nama hero: {self.name}, health: {self.health}, attack: {self.attack}, armor: {self.armor}, mana: {self.mana}, range: {self.range}"

balmond = hero("Balmond", 100, 15, 4) 
layla = mmaksman("Layla", 80, 20, 2)
print(balmond)
print(layla) 