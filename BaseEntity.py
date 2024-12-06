from CombatState import CombatStateMachine

class Entity(CombatStateMachine):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__()
        self.__name = name
        self.__hp = hp
        self.__DMG = DMG
        self.__stamina = stamina
        self.__guard = False
        self.count = 0
        self.__max_hp = hp
        self.__max_stamina = stamina
        self.__max_DMG = DMG
    def get_name(self):
        return f"{self.__name}"
    def use_energy(self):
        self.__stamina -= 5
    def set_hp(self, amount):
        self.__hp += amount
    def get_hp(self):
        return self.__hp
    def get_DMG(self):
        return self.__DMG
    def set_DMG(self, amount):
        self.__DMG = amount
    def set_stamina(self, amount):
        self.__stamina += amount
    def get_stamina(self):
        return self.__stamina
    def set_guard(self, Boolean):
        self.__guard = Boolean
    def get_guard(self):
        return self.__guard
    def recover(self):
        self.__stamina = 100
    def get_max_hp(self):
        return self.__max_hp
    def get_max_DMG(self):
        return self.__max_DMG
    def get_max_stamina(self):
        return self.__max_stamina