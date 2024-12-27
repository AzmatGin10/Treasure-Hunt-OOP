import questionary
from rich.console import Console
from rich.progress import Progress
from rich import print
from BaseEntity import Entity
from Items import Item, Weapon, Armour, HealingItem, CreateRandomWeapon
from clear import clear_console
import getch 
console = Console()

class Player(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
        self.currentweapon = ""
        self.currentarmour = ""
        self.inventory = []
    def equip(self, item):
        if type(item) == Weapon:
            if self.currentweapon == "":
                self.set_DMG(item.get_DMG())
                self.currentweapon = item
                self.inventory.append(item)
            else:
                self.set_DMG(self.currentweapon.get_DMG()*-1)
                self.set_DMG(item.get_DMG())
                self.currentweapon = item
                self.inventory.append(item)
        elif type(item) == Armour:
            if self.currentarmour == "":
                self.set_hp(item.get_def())
                self.currentarmour = item
                self.inventory.append(item)
                
            else:
                self.set_hp(self.currentarmour.get_def()*-1)
                self.set_hp(item.get_def())
                self.currentarmour = item
                self.inventory.append(item)
                
        else:
            input("This is not a compatible usage of the equip function")
        
        
        pass
    def pick_up(self, object):
        if len(self.inventory)<=10:
            self.inventory.append(object)
        else:
            raise Exception("Inventory is already full")
    def drop_item(self, object):
        if object in self.inventory:
            self.inventory.remove(object)
        else:
            raise Exception("An issue occured")
    def heal(self, item):
        self.set_hp(item)
    def get_max_health(self):
        if self.currentarmour != "":
            return self.get_max_hp() + self.currentarmour.get_def()
        return self.get_max_hp()
    
    def defend(self):

        self.set_guard(True)

    def view_stats(self):
    
        with Progress(console=console) as progress:
            progress.add_task("[bold red]HP", total=self.get_max_health(), completed=self.get_hp())
            progress.add_task("[bold green]Stamina", total=self.get_max_stamina(), completed=self.get_stamina())
            progress.add_task("[bold purple]DMG", total=self.get_max_DMG(), completed=self.get_DMG())
            
    def view_enemy(self, enemy):
        with Progress(console=console) as progress:
            progress.add_task("[bold red]HP", total=enemy.get_max_hp(), completed=enemy.get_hp())
            progress.add_task("[bold green]Stamina", total=enemy.get_max_stamina(), completed=enemy.get_stamina())
            progress.add_task("[bold purple]DMG", total=enemy.get_max_DMG(), completed=enemy.get_DMG())
    def loadout(self):
        clear_console()
        response = questionary.select(
            "What would you like to check?",
            choices=[
                "Check Current Loadout",
                "Check Items",
                "Check Weapons",
                "Check Armour",
                "Equip from inventory",
                "Drop Items",
                "Back..."
            ]).ask() 
        
        if response == "Check Current Loadout":
            clear_console()
            print(f"Your current Weapon is: [bold red]{self.currentweapon.get_desc()}[/bold red]\nYour current Armour is: [bold purple]{self.currentarmour.get_desc()}[/bold purple]")
            PlayerInput = getch.getch()
            if PlayerInput:
                return self.loadout()
            
        elif response == "Check Items":
            clear_console()
            for item in self.inventory:
                if isinstance(item, HealingItem):
                    print(f"[bold blue]{item.get_desc()}[/bold blue]")
            PlayerInput = getch.getch()
            if PlayerInput:
                return self.loadout()
        elif response == "Check Weapons":
            clear_console()
            for item in self.inventory:
                if isinstance(item, Weapon):
                    print(f"[bold red]{item.get_desc()}[/bold red]")
            PlayerInput = getch.getch()
            if PlayerInput:
                return self.loadout()
        elif response == "Check Armour":
            clear_console()
            for item in self.inventory:
                if isinstance(item, Armour):
                    print(f"[bold purple]{item.get_desc()}[/bold purple]")
            PlayerInput = getch.getch()
            if PlayerInput:
                return self.loadout()
        if response == "Equip from inventory":
            clear_console()
            
            
            response = questionary.select(
                "What would you like to equip?",
                choices=[
                    "Weapon",
                    "Armour",
                    "Back"
                ]
            ).ask()
            if response == "Weapon":
                clear_console()
                print(f"Your current Weapon is: [bold red]{self.currentweapon.get_desc()}[/bold red]")
                weapons = [item for item in self.inventory if isinstance(item, Weapon)]
                choices = [item.get_desc() for item in self.inventory if isinstance(item, Weapon)]
                response = questionary.select(
                    "Available Weapons...",
                    choices=[item.get_desc() for item in self.inventory if isinstance(item, Weapon)]
                ).ask()
                clear_console()
                chosen_weapon = weapons[choices.index(response)]
                self.equip(chosen_weapon)
                print(f"You have now equiped The [bold red]{chosen_weapon.get_name()}[/bold red]")
                PlayerInput = getch.getch()
                if PlayerInput:
                    return self.loadout()
            elif response == "Armour":
                clear_console()
                print(f"Your current Armour is: [bold purple]{self.currentarmour.get_desc()}[/bold purple]")
                armours = [item for item in self.inventory if isinstance(item, Armour)]
                choices = [item.get_desc() for item in self.inventory if isinstance(item, Armour)]
                response = questionary.select(
                    "Available Armour...",
                    choices=[item.get_desc() for item in self.inventory if isinstance(item, Armour)]
                    ).ask()
                clear_console()
                chosen_armour = armours[choices.index(response)]
                self.equip(chosen_armour)
                print(f"You have now equiped The [bold purple]{chosen_armour.get_name()}[/bold purple]")
                PlayerInput = getch.getch()

                if PlayerInput:
                    return self.loadout()
            else:
                return self.loadout()
        if response == "Drop Items":
            if len(self.inventory) > 0:
                items = [x for x in self.inventory]
                choices = [item.get_name() for item in self.inventory]
                choices.append("Back")
                response = questionary.select(
                    "What would you like to drop",
                    choices=choices
                ).ask()
                if response == "Back":
                    return self.loadout()
                chosen_item = items[choices.index(response)]
                self.drop_item(chosen_item)
                print(f"You have dropped {response}")
                PlayerInput = getch.getch()
                if PlayerInput:
                    return self.loadout()
            else:
                print("You have no items!")
                PlayerInput = getch.getch()
                if PlayerInput:
                    return self.loadout()
        else:
            pass
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
random_dagger = CreateRandomWeapon(0)
random_stick = CreateRandomWeapon(3)
dagger1 = random_dagger.make_weapon()
dagger2 = random_dagger.make_weapon()
armour1 = Armour(2)
armour2 = Armour(1)
Heal1 = HealingItem(2)
player.pick_up(Heal1)
player.equip(dagger1)
player.equip(dagger2)
player.equip(armour1)
player.equip(armour2)


#print(player.view_stats())
#print(player.currentweapon.get_desc())
#player.loadout()

""""
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
    
"""
