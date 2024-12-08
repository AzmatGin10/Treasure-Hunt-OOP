class Weapon():
    def __init__(self, name, DMG):
        self.__DMG = DMG
        self.name = name
    def get_DMG(self):
        return self.__DMG
    def get_desc(self):
        return "this is a weapon"
    
class Armour():
    def __init__(self, name, hp):
        self.__hp = hp
    def get_hp(self):
        return self.__hp
    def get_desc(self):
        return "This is armour"
    
class HealingItem():
    def __init__(self):
        self._heal = 0
    def get_heal(self):
        return self._heal
    def get_desc(self):
        return "This is a healing item"


class Healing_Flask(HealingItem):
    def __init__(self):
        super().__init__()
        self._heal = 50
    def get_desc(self):
        return "This is a Healing Flask: Restores 50hp."
class Greater_Healing_Flask(HealingItem):
    def __init__(self):
        super().__init__()
        self._heal = 100
    def get_desc(self):
        return "This is a Greater Healing Flask: Restores 100hp!"
class Lesser_Healing_Flask(HealingItem):
    def __init__(self):
        super().__init__()
        self._heal = 25
    def get_desc(self):
        return "This is a Lesser Healing Flask: Restores 25hp..."

class Dagger(Weapon):
    def __init__(self, name, DMG):
        super().__init__(name, DMG)
    def get_desc(self):
        return f"This is the {self.name}: It deals {self.get_DMG()} Damage"
class Stick(Weapon):
    def __init__(self, name, DMG):
        super().__init__(name, DMG)
    def get_desc(self):
        return f"This is the {self.name}: It deals {self.get_DMG()} Damage"
class Sword(Weapon):
    def __init__(self, name, DMG):
        super().__init__(name, DMG)
    def get_desc(self):
        return f"This is the {self.name}: It deals {self.get_DMG()} Damage"
class Katana(Weapon):
    def __init__(self, name, DMG):
        super().__init__(name, DMG)
    def get_desc(self):
        return f"This is the {self.name}: It deals {self.get_DMG()} Damage"


class IronArmour(Armour):
    def __init__(self, name, hp):
        super().__init__(name, hp)
    def get_desc(self):
        return f"This is {self.name}: It adds {self.get_DMG()} HP"
class BedSheets(Armour):
    def __init__(self, name, hp):
        super().__init__(name, hp)
    def get_desc(self):
        return f"This is {self.name}: It adds {self.get_DMG()} HP"
class HelmetOfVitality(Armour):
    def __init__(self, name, hp):
        super().__init__(name, hp)
    def get_desc(self):
        return f"This is {self.name}: It adds {self.get_DMG()} HP"

