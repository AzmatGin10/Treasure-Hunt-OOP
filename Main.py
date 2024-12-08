import random

class Item:
    def __init__(self, name, desc):
        self.__name = name
        self.__desc = desc
        
    def get_name(self):
        return self.__name
    
    def get_desc(self):
        return self.__desc
    
class Weapon(Item):
    def __init__(self, names, dmg):
        name = names[random.randint(0, len(names)-1)]
        super().__init__(name, f"This is the {name}: It deals {dmg} Damage")
        self.__dmg = dmg
        
    def get_DMG(self):
        return self.__dmg
    
class Armour(Item):
    def __init__(self, names, hp):
        name = names[random.randint(0, len(names)-1)]
        super().__init__(name, f"This is {name}: It adds {hp} HP")
        self.__hp = hp
        
    def get_hp(self):
        return self.__hp
    
class HealingItem(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, f"This is a {name}: Restores {heal_amount} HP.")
        self.__heal_amount = heal_amount
        
    def get_heal(self):
        return self.__heal_amount
    
