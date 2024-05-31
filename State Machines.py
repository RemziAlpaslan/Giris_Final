startState = "waiting"

def generateOutput(self, state):
    if state == "raising":
        return "raise"
    elif state == "lowering":
        return "lower"
    else:
        return "nop"

def getNextValues(self, state, inp):
    (gatePosition, carAtGate, carJustExited) = inp
    if state == "waiting" and carAtGate:
        nextState = "raising"
    elif state == "raising" and gatePosition == "top":
        nextState = "raised"
    elif state == "raised" and carJustExited:
        nextState = "lowering"
    elif state == "lowering" and gatePosition == "bottom":
        nextState = "waiting"
    else:
        nextState = state
    return (nextState, self.generateOutput(nextState))

