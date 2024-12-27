import random
from rich import print
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
        super().__init__(name, f"The {name}: It deals {self.get_DMG()} Damage")
    def get_DMG(self):
        return self.__DMG

class Armour(Item):

    def __init__(self, type):
        type_1 = ("Blanket", 50)                #name, hp
        type_2 = ("Cat Disguise", 100)
        type_3 = ("Typical School Uniform", 200)
        self.type = {
            0: type_1,
            1: type_2,
            2: type_3,
        }.get(type)
        super().__init__(self.type[0], f"The {self.type[0]}: It adds {self.type[1]} HP")
        self.__hp = self.type[1]

    def get_def(self):
        return self.__hp
    
class HealingItem(Item):
    def __init__(self, type):
        type_1 = ("Small Healing Flask", 50) #Name, Healing amount
        type_2 = ("Medium Healing Flask", 100)
        type_3 = ("Large Healing Flask", 150)
        self.type = {
            0: type_1,
            1: type_2,
            2: type_3
        }.get(type)

        super().__init__(self.type[0], f"A {self.type[0]}: Restores {self.type[1]} HP.")
        self.__heal_amount = self.type[1]
        
    def get_heal(self):
        return self.__heal_amount
class CreateRandomWeapon():   
    def __init__(self, type):
        self.type = type
        
        self.weapon_names ={
        "dagger" : [("Dagger of Respite", 20), ("Broken Dagger", 10), ("Holy Dagger", 25), ("Daggerfall", 30), ("Ordinary Dagger", 15)],
        "sword" : [("Silver Sword", 30), ("Broken Sword", 25), ("Sword of The Fallen King", 40), ("Ordinary Sword", 30)],
        "katana" :  [("Issei no Katana", 40), ("Samurais's Hope", 35), ("Abyssal Blade", 50), ("夜の剣", 55), ("Ordinary Katana", 30) ],
        "stick" : [("Stick of Doom", 50), ("Brownest Stick", 60), ("Stick of Calamity", 80), ("STICKY situation", 55), ("Simple Stick", 100)]
    }
        self.chosen_weapon = list(self.weapon_names.keys())[self.type]
    def make_weapon(self):
        if self.type == 0:
            return Weapon(self.weapon_names[self.chosen_weapon][random.randint(0, len(self.weapon_names[self.chosen_weapon])-1)])
        elif self.type == 1:
            return Weapon(self.weapon_names[self.chosen_weapon][random.randint(0, len(self.weapon_names[self.chosen_weapon])-1)])
        elif self.type == 2:
            return Weapon(self.weapon_names[self.chosen_weapon][random.randint(0, len(self.weapon_names[self.chosen_weapon])-1)])
        elif self.type == 3:
            return Weapon(self.weapon_names[self.chosen_weapon][random.randint(0, len(self.weapon_names[self.chosen_weapon])-1)])
        else:
            raise Exception("You fool, you did something wrong")

        
