class CombatState:
    def __init__(self, context):
        self.context = context
    def OnEnter(self):
        pass
class ActiveState(CombatState):
    #overriding
    def OnEnter(self):
        return "tired"

class TiredState(CombatState):
    #overriding
    def OnEnter(self):
        return "collapsed"
class CollapsedState(CombatState):
    #overriding
    def OnEnter(self):
        return "active"
class CombatStateMachine:
    def __init__(self):
        self.states = {
            "active" : ActiveState(self),
            "tired" : TiredState(self),
            "collapsed" : CollapsedState(self)
        }        
        self.currentstate = "active"
    def TransitionState(self):
        nextstate = self.states[self.currentstate].OnEnter()
        if self.currentstate != nextstate:
            self.currentstate = nextstate

