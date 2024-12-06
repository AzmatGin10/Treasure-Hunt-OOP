class State:
    def __init__(self, context):
        self.context = context
    def OnEnter(self):
        pass
class ActiveState(State):
    #overriding
    def OnEnter(self):
        
        return "tired"
class TiredState(State):
    #overriding
    def OnEnter(self):
        return "active"
class CombatStateMachine:
    def __init__(self):
        self.states = {
            "active" : ActiveState(self),
            "tired" : TiredState(self)
        }        
        self.currentstate = "active"
    def TransitionState(self):
        nextstate = self.states[self.currentstate].OnEnter()
        if self.currentstate != nextstate:
            self.currentstate = nextstate
