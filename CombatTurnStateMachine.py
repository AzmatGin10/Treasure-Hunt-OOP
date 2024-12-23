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

class BaseCombatState():
    def __init__(self, context, player, enemy):
       self.context = context
       self.player = player
       self.enemy = enemy
    def OnEnter(self):
        pass

class ChooseActionState(BaseCombatState):
    def OnEnter(self):
        return "implement"
class ImplementActionState(BaseCombatState):
    def OnEnter(self):
        return "choose"

class CombatTurnStateMachine():
    def __init__(self):
        self.states = {
            "choose" : ChooseActionState().OnEnter(),
            "implement" : ImplementActionState().OnEnter()
        }
        self.currentstate = "choose"
    def TransitionState(self):
        pass
