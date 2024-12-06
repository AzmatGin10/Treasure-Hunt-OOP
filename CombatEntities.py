import questionary
from rich.console import Console
from rich.progress import Progress
from CombatState import CombatStateMachine
from BaseEntity import Entity



console = Console()

class Player(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
        self.__max_hp = hp
        self.__max_stamina = stamina
        self.__max_DMG = DMG 
    def heal(self, item):
        self.set_hp(item)
    def attack(self, enemy):
        
        if self.currentstate == "active":
            enemy.set_hp(self.get_DMG()*-1 if not enemy.get_guard() else self.get_DMG()/2*-1)
            self.use_energy()
            if self.get_stamina() <= 50:
                self.TransitionState()
        else:
            self.count += 1
            enemy.set_hp(self.get_DMG()/2) 
            self.use_energy()
            if self.count == 3:
                self.TransitionState()
                self.count = 0
                self.recover()
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
    
class Enemy(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
    def attack(self, player):
        
        if self.currentstate == "active":
            player.set_hp(self.get_DMG()*-1 if not player.get_guard() else self.get_DMG()/2*-1)
            self.use_energy()
            if self.get_stamina() <= 50:
                self.TransitionState()
        else:
            self.count += 1
            player.set_hp(self.get_DMG()/2)
            self.use_energy()
            if self.count == 3:
                self.TransitionState()
                self.count = 0
                self.recover()
class Boss(Entity):
    def __init__(self, name, hp, DMG, stamina):
        super().__init__(name, hp, DMG, stamina)
        self.count = 0
    def heal(self):
        self.set_hp(10)
    def defend(self):
        self.get_guard = True
    def attack(self, player):
        
        if self.currentstate == "active":
            player.set_hp(self.get_DMG()*-1 if not player.get_guard() else self.get_DMG()/2*-1)
            self.use_energy()
            if self.get_stamina() <= 50:
                self.TransitionState()
        else:
            self.count += 1
            player.set_hp(self.get_DMG()/2)
            self.use_energy()
            if self.count == 3:
                self.TransitionState()
                self.count = 0
                self.recover()




player = Player("Ryan", 200, 20, 100)
enemy = Player("Skeleton", 100, 10, 100)
player.view_enemy(enemy)
##print(player.get_stamina())
#print(player.currentstate)
#player.view_stats()
player.attack(enemy)
#print(player.currentstate)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
#print(player.get_stamina())
#print(player.currentstate)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
#print(player.get_stamina())
#print(player.currentstate)
#player.view_stats()



    
