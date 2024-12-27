import questionary

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

class Player:
    def __init__(self):
        pass
    def get_hp(self):
        return 100
    def get_max_hp(self):
        return 100
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
            return "Your Health is dropping! Perhaps you should play defensively"
        else:
            return "You are ready to fight!"
    def OnEnter(self):
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
        return move
    def CycleState(self):
        return "implement"
class ImplementActionState(BaseCombatState):
    def __init__(self, context, player, enemy):
        super().__init__(context, player, enemy)
    def OnEnter(self):
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
    def TransitionState(self):
        nextstate = self.states[self.currentstate].CycleState()
        if self.currentstate != nextstate:
            self.currentstate = nextstate



pla = Player()
state = CombatTurnStateMachine(pla, "test")
while True:
    state.Choose()
    break