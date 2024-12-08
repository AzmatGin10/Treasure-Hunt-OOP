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
    def __init__(self, names, DMGS):
        name = names[random.randint(0, len(names)-1)]
        DMG = DMGS[random.randint(0, len(DMGS)-1)]
        self.__DMG = DMG
        super().__init__(name, f"This is the {name}: It deals {DMG} Damage")
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
        self.name = name
        self.weapon_names ={
        "dagger" : ["Dagger of Respite", "Broken Dagger", "Holy Dagger"],
        "sword" : ["Silver Sword", "Broken Sword", "Sword of The Fallen King"],
        "katana" :  ["Issei no Katana", "Samurais's Hope", "Abyssal Blade", "夜の剣"],
        "stick" : ["Stick of Doom", "Brownest Stick", "Stick of Calamity"]
    }
        self.weapons_stats = {

            "dagger" : [10, 20, 15],
            "sword" : [20, 30, 40, 35],
            "katana" :  [40, 30, 50, 55],
            "stick" : [40, 60 ,80, 70]
            }
    def get_name(self):
        return self.weapon_names[self.name]
    def get_DMG(self):
        return self.weapons_stats[self.name]
    def make_weapon(self):
        return Weapon(self.get_name(), self.get_DMG())

