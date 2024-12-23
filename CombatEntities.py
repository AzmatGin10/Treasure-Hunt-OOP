import questionary
from rich.console import Console
from rich.progress import Progress
from BaseEntity import Entity
from Items import Item, Weapon, Armour, HealingItem, CreateRandomWeapon

console = Console()

class Player(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
        self.currentweapon = ""
        self.currentarmour = ""
        self.inventory = []
    def equip_weapon(self, weapon):
        if len(self.inventory) < 10:
            if self.currentweapon == "":
                self.set_DMG(weapon.get_DMG())
                self.currentweapon = weapon
                self.inventory.append(weapon)
            else:
                self.set_DMG(self.currentweapon.get_DMG()*-1)
                self.set_DMG(weapon.get_DMG())
                self.currentweapon = weapon
                self.inventory.append(weapon)
        else:
            pass
    def equip_armour(self, armour):
        if len(self.inventory) < 10:
                
            if self.currentarmour == "":
                self.set_hp(armour.get_hp())
                self.currentarmour = armour
                self.inventory.append(armour)
            else:
                self.set_hp(self.currentarmour.get_hp()*-1)
                self.set_hp(armour.get_hp())
                self.currentarmour = armour
                self.inventory.append(armour)
        else:
            pass
    def heal(self, item):
        self.set_hp(item)
    
    def defend(self):
        self.set_guard(True)
    def view_stats(self):
    
        with Progress(console=console) as progress:
            progress.add_task("[bold red]HP", total=self.get_max_hp(), completed=self.get_hp())
            progress.add_task("[bold green]Stamina", total=self.get_max_stamina(), completed=self.get_stamina())
            progress.add_task("[bold purple]DMG", total=self.get_max_DMG(), completed=self.get_DMG())
            
    def view_enemy(self, enemy):
        with Progress(console=console) as progress:
            progress.add_task("[bold red]HP", total=enemy.get_max_hp(), completed=enemy.get_hp())
            progress.add_task("[bold green]Stamina", total=enemy.get_max_stamina(), completed=enemy.get_stamina())
            progress.add_task("[bold purple]DMG", total=enemy.get_max_DMG(), completed=enemy.get_DMG())
    def loadout(self):
        return f"Current Weapon: {self.currentweapon.get_name()}\nCurrent Armour {self.currentarmour}\nInventory: {[item.get_name() for item in self.inventory]}"
        
class Enemy(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
    
class Boss(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
    def heal(self):
        self.set_hp(10)
    def defend(self):
        self.get_guard = True
    def big_attack(self, player):
        player.set_hp(self.get_DMG()*-5 if not player.get_guard() else self.get_DMG()*-2)  



player = Player("Ryan", 200, 20, 100)
enemy = Player("Skeleton", 100, 10, 100)
boss = Boss("Ogre", 500, 20, 10)
random_dagger = CreateRandomWeapon("dagger")
random_stick = CreateRandomWeapon("stick")
dagger1 = random_dagger.make_weapon()
dagger2 = random_dagger.make_weapon()
player.equip_weapon(dagger1)

print(player.view_stats())
print(player.currentweapon.get_desc())
while True:
    userInput = input("1 is player attack boss, 2 is boss attack player, 3 is a big attack")
   
    if userInput == "1":
        player.attack(boss)
        print(boss.get_hp())
    if userInput == "2":
        boss.attack(player)
        print(player.get_hp())
    if userInput == "3":
        boss.big_attack(player)
        print(player.get_hp())
    if player.get_hp() <= 0:
        print("Player has died")
        break
    if boss.get_hp() <= 0:
        print("boss has died")
        break
    

