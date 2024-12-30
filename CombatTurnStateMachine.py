import questionary
from CombatEntities import Player, Enemy
from System import clear_console
import getch
from Items import HealingItem, Weapon, Armour, CreateRandomWeapon
import random
import time
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
    def Random_Attack_Message(self):
        probabilitity = [60, 25, 10, 5]
        prob_total = 100 - random.randint(0, 100)
        i = len(probabilitity) - 1
        prompts = {
            0: f"You attacked {self.enemy.get_name()}! ",
            1: f"With a Single, Smooth, Fluid act, You attacked {self.enemy.get_name()}!",
            2: f"With Determination burning through your Soul, You delivered a Strike to The {self.enemy.get_name()}!",
            3: f"YOu BonKeD ThE {self.enemy.get_name()}! YoU FeLT VeRy HappinEsS. Yay!"
        }
        for prob in probabilitity:
            if prob_total <= probabilitity[i]:
                return prompts[i]
            else:
                prob_total -= probabilitity[i]
                i -= 1
    def Random_Enemy_Message(self):
        probabilitity = [60, 25, 10, 5]
        prob_total = 100 - random.randint(0, 100)
        i = len(probabilitity) - 1
        prompts = {
            0: f"The {self.enemy.get_name()} attacked you!",
            1: f"The {self.enemy.get_name()} charged at you with a Shrill Cry!",
            2: f"The {self.enemy.get_name()} lunged at you with intent to harm!",
            3: f"The {self.enemy.get_name()} attacked you unwillingly, with face of Sadness"
        }
        for prob in probabilitity:
            if prob_total <= probabilitity[i]:
                return prompts[i]
            else:
                prob_total -= probabilitity[i]
                i -= 1
    def Random_Defense_Message(self):
        probabilitity = [60, 25, 10, 5]
        prob_total = 100 - random.randint(0, 100)
        i = len(probabilitity) - 1
        prompts = {
            0: f"You took on a defensive stance. Attacks will now deal less damage to you!",
            1: f"Like water, your body flowed into a single drop. You have entered the Water Defense!",
            2: f"Fire raging within you, You felt a wall of Flames guard you!",
            3: f"With the power of the Sky, Earth and Sea. All attacks before you are akin to that of a child. You have entered the Defense Flow State!"
        }  
        for prob in probabilitity:
            if prob_total <= probabilitity[i]:
                return prompts[i]
            else:
                prob_total -= probabilitity[i]
                i -= 1
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
                "Heal",
                "View Player",
                "View Enemy",
                "Loadout"
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
        elif move == "Heal":
            clear_console()
            choices = [item for item in self.player.inventory if isinstance(item, HealingItem)]
            display = [item.get_desc() for item in choices]
            display.append("Back")
            if len(choices) == 0:
                print("You have no Healing items!")  
                PlayerInput = getch.getch()
                if PlayerInput:
                    return self.OnEnter()  
            else:
                response = questionary.select(
                    "Choose a Healing item",
                    choices=display
                ).ask()
                if response == "Back":
                    return self.OnEnter()
                chosen_heal = choices[display.index(response)]
                self.player.heal(chosen_heal)
                
                print(f"You took a {chosen_heal.get_name()}. You feel Rejuvenated!")
                PlayerInput = getch.getch()
                if PlayerInput:
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
        if player_move == "defend":
            self.player.defend()
            print(self.Random_Defense_Message())
            time.sleep(3)
        if enemy_move == 1:
            self.enemy.set_guard(True)
            print(f"{self.enemy.get_name()} went on the defensive!")
            time.sleep(3)
        if player_move == "attack":
            self.player.attack(self.enemy)
            print(self.Random_Attack_Message())
            time.sleep(3)
        
        if enemy_move == 0:
            self.enemy.attack(self.player)
            print(self.Random_Enemy_Message())
            time.sleep(3)
        
        if enemy_move == 2:
            print(f"{self.enemy.get_name()} stared at you menacingly... But He didn't seen to do anything?")
            time.sleep(3)
        
        
        self.player.set_guard(False)
        self.enemy.set_guard(False)
        
    def CycleState(self):
        return "choose"
class CombatTurnStateMachine():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.states = {
            "choose" : ChooseActionState(self, player, enemy),
            "implement" : ImplementActionState(self, player, enemy)
        }
        self.currentstate = "choose"
    def Choose(self):
        return self.states["choose"].OnEnter()
    def Implement(self, player_move):
        return self.states["implement"].OnEnter(player_move)
    def Check_Battle_Status(self):
        if self.player.get_hp() <= 0:
            print("You lose!")
            return "lose"
        elif self.enemy.get_hp() <= 0:
            print("You win!")
            return "win"
        else:
           pass 
    def TransitionState(self):
        nextstate = self.states[self.currentstate].CycleState()
        if self.currentstate != nextstate:
            self.currentstate = nextstate



player = Player("Bob", 200, 20, 100)
enemy = Enemy(4)
random_weapon = CreateRandomWeapon(1)
heal = HealingItem(2)
player.pick_up(random_weapon.make_weapon())
player.pick_up(heal)
state = CombatTurnStateMachine(player, enemy)

#for tomorrow, add healing to the loadout, add proper ui for the fighting, add a way for the fight to end