import questionary
from CombatEntities import Player, Enemy
from clear import clear_console
import getch
from Items import HealingItem, Weapon, Armour, CreateRandomWeapon
#has a player and an enemy
#takes an input from player and random move from enemy
#needs a store for all moves
#ChooseAction state
#ImplementAction state
#keep track of health
#Have a reset fight option or lose game
#In the while loop make sure it shows a little display for health
#1) Needs a base state
#2) inheriting from it is chooseaction state and implement action state
#3) statemachine holding all states and curretn state
#4) transition state => Change state when recieved correct input
#5) a main loop for choices and interface and actual combat inherits statemachine
#6) choose state needs to constanlty check healths so win or lose will be shown in choose state
# choose state fleshing out:
#Needs to give feedback on player health, perhaps giving advice on moves for moves
# Have 5 options of moves => Attack, defend, view player, view enemy, items
# Choose state only ends if you commit to an attack or defend
# attack => simply asks whether you wish to attack the enemy
# defend => simply asks whetehr you wish to attack the enemy
# view player =? views player stats
# view enemy => view enemy stats
# items => consumable for health 


class BaseCombatState():
    def __init__(self, context, player, enemy):
       self.context = context
       self.player = player
       self.enemy = enemy
    def OnEnter(self):
        pass
    def CycleState(self):
        pass
class ChooseActionState(BaseCombatState):
    def __init__(self, context, player, enemy):
        super().__init__(context, player, enemy)
    def HealthLevel(self):
        if ((self.player.get_hp()/self.player.get_max_hp())*100) <= 25:
            return "Your Health is looking Low! Maybe a healing item is in order?"
        elif ((self.player.get_hp()/self.player.get_max_hp())*100) <= 50:
            return "Your Health is dropping low! Perhaps you should play defensively"
        else:
            return "You are ready to fight!"
        
    def OnEnter(self):
        clear_console()
        move = questionary.select(
            self.HealthLevel(),
            choices = [
                "Attack", 
                "Defend",
                "View Player",
                "View Enemy",
                "Loadout",
            ]
        ).ask()
        if move == "Attack":
            clear_console()
            response = questionary.confirm("Are you sure you would like to attack?").ask()
            if response:
                return "attack"
            else:
                return self.OnEnter()
            
        elif move == "Defend":
            clear_console()
            response = questionary.confirm("Are you sure you would like to defend?").ask()
            if response:
                return "defend"
            else:
                return self.OnEnter()
            
        elif move == "View Player":
            clear_console()
            print(f"Now viewing {self.player.get_name()}...")
            self.player.view_stats()
            PlayerInput = getch.getch()
            if PlayerInput:
                return self.OnEnter()
            
        elif move == "View Enemy":
            clear_console()
            print(f"Now viewing {self.enemy.get_name()}...")
            self.player.view_enemy(self.enemy)
            PlayerInput = getch.getch()
            if PlayerInput:
                return self.OnEnter()
           
        elif move == "Loadout":
            self.player.loadout()
            return self.OnEnter()
        
    def CycleState(self):
        return "implement"
class ImplementActionState(BaseCombatState):
    def __init__(self, context, player, enemy):
        super().__init__(context, player, enemy)
    def OnEnter(self, player_move):
        enemy_move = self.enemy.random_move()
        if enemy_move == 0:
            self.enemy.attack(self.player)
            print(f"{self.enemy.get_name()} attacked you!")
        if enemy_move == 1:
            self.enemy.defend()
            print(f"{self.enemy.get_name()} went on the defensive!")
        if enemy_move == 2:
            print(f"{self.enemy.get_name()} stared at you menacingly")
        if player_move == "attack":
            self.player.attack(self.enemy)
            print(f"You attacked {self.enemy.get_name()}!")
        if player_move == "defend":
            self.player.defend()
            print(f"You took a defensive stance! Attacks will affect you significntly less now.")
        PlayerInput = getch.getch()
        if PlayerInput:
            pass
    def CycleState(self):
        return "choose"
class CombatTurnStateMachine():
    def __init__(self, player, enemy):
        self.states = {
            "choose" : ChooseActionState(self, player, enemy),
            "implement" : ImplementActionState(self, player, enemy)
        }
        self.currentstate = "choose"
    def Choose(self):
        return self.states["choose"].OnEnter()
    def Implement(self, player_move):
        return self.states["implement"].OnEnter(player_move)
    def TransitionState(self):
        nextstate = self.states[self.currentstate].CycleState()
        if self.currentstate != nextstate:
            self.currentstate = nextstate



player = Player("Bob", 200, 20, 100)
enemy = Enemy("Skeleton", 100, 10, 50)
random_weapon = CreateRandomWeapon(1)
heal = HealingItem(2)
player.pick_up(random_weapon.make_weapon())
player.pick_up(heal)
state = CombatTurnStateMachine(player, enemy)
#while True:
   # player_move = state.Choose()
   # state.TransitionState()
   # state.Implement(player_move)
#for tomorrow, add healing to the loadout, add proper ui for the fighting, add a way for the fight to end