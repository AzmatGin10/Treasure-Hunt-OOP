import random
weapons_names = {
        "dagger" : ["Dagger of Respite", "Broken Dagger", "Holy Dagger"],
        "sword" : ["Silver Sword", "Broken Sword", "Sword of The Fallen King"],
        "katana" :  ["Issei no Katana", "Samurais's Hope", "Abyssal Blade", "夜の剣"],
        "stick" : ["Stick of Doom", "Brownest Stick", "Stick of Calamity"]
    }
class Item:
    def __init__(self, name, desc):
        self.__name = name
        self.__desc = desc
        
    def get_name(self):
        return self.__name
    
    def get_desc(self):
        return self.__desc
class Weapon(Item):
    def __init__(self, weapon):
        name = weapon[0]
        self.__DMG = weapon[1]
        super().__init__(name, f"This is the {name}: It deals {self.get_DMG()} Damage")
    def get_DMG(self):
        return self.__DMG
    
class Armour(Item):
    def __init__(self, names, hp):
        name = names[random.randint(0, len(names)-1)]
        super().__init__(name, f"This is The {name}: It adds {hp} HP")
        self.__hp = hp
        
    def get_hp(self):
        return self.__hp
    
class HealingItem(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, f"This is a {name}: Restores {heal_amount} HP.")
        self.__heal_amount = heal_amount
        
    def get_heal(self):
        return self.__heal_amount
class CreateRandomWeapon():   
    def __init__(self, name):
        self.chosen_weapon = name
        self.weapon_names ={
        "dagger" : [("Dagger of Respite", 20), ("Broken Dagger", 10), ("Holy Dagger", 25), ("Daggerfall", 30), ("Ordinary Dagger", 15)],
        "sword" : [("Silver Sword", 30), ("Broken Sword", 25), ("Sword of The Fallen King", 40), ("Ordinary Sword", 30)],
        "katana" :  [("Issei no Katana", 40), ("Samurais's Hope", 35), ("Abyssal Blade", 50), ("夜の剣", 55), ("Ordinary Katana", 30) ],
        "stick" : [("Stick of Doom", 50), ("Brownest Stick", 60), ("Stick of Calamity", 80), ("STICKY situation", 55), ("Simple Stick", 100)]
    }
    def make_weapon(self):
        return Weapon(self.weapon_names[self.chosen_weapon][random.randint(0, len(self.weapon_names[self.chosen_weapon])-1)])
dagger = CreateRandomWeapon("dagger")
dagger1 = dagger.make_weapon()
dagger2 = dagger.make_weapon()
print(dagger1.get_name())
print(dagger1.get_DMG())
print(dagger2.get_name())

print(dagger2.get_DMG())
print(dagger1.get_desc())