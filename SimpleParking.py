def generateOutput(state):
    if state == "raising":
        return "raise"
    elif state == "lowering":
        return "lower"
    else:
        return "nop"

def getNextValues(state, gatePosition, carAtGate ,carJustExited ):
    carAtGate=str(carAtGate)
    carJustExited =str(carJustExited )
    if state == "waiting" and carAtGate == "True":
        nextState = "raising"
    elif state == "raising" and gatePosition == "top":
        nextState = "raised"
    elif state == "raised" and carJustExited == "True":
        nextState = "lowering"
    elif state == "lowering" and gatePosition == "bottom":
        nextState = "waiting"
    else:
        nextState =state
    return (generateOutput(nextState),nextState)

def GetNextState(state, gatePosition, carAtGate ,carJustExited ):
    carAtGate=str(carAtGate)
    carJustExited =str(carJustExited )
    if state == "waiting" and carAtGate == "True":
        nextState = "raising"
    elif state == "raising" and gatePosition == "top":
        nextState = "raised"
    elif state == "raised" and carJustExited == "True":
        nextState = "lowering"
    elif state == "lowering" and gatePosition == "bottom":
        nextState = "waiting"
    else:
        nextState =state
    return nextState

def  SimpleParkingGate(state, gatePosition, carAtGate ,carJustExited):
    print(getNextValues(state, gatePosition, carAtGate ,carJustExited ))
    return (SimpleParkingGate(GetNextState(state, gatePosition, carAtGate ,carJustExited), input("gatePosition:",), input("carAtGate:") ,input("carJustExited:")))

SimpleParkingGate("waiting", "bottom", False ,False)