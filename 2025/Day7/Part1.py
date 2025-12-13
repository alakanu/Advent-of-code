filePath = "TachyonManifold.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    stages = fileContent.splitlines()
    stageSize = len(stages[0])
    stagesCount = len(stages)
    previousState = [c if c == "." else "|" for c in stages[0]]
    beam = "|"
    emptySpace = "."
    splitter = "^"
    splitCount = 0

    for stageIndex in range(1, stagesCount):
        newState = []
        pendingBeamAppend = False
        for i in range(0, stageSize):
            if pendingBeamAppend:
                newState.append(beam)
                pendingBeamAppend = False
                continue
            if stages[stageIndex][i] == emptySpace:
                newState.append(previousState[i])
            elif stages[stageIndex][i] == splitter:
                if previousState[i] == beam:
                    splitCount = splitCount + 1
                    newState[i - 1] = beam
                    newState.append(emptySpace)
                    pendingBeamAppend = True
                else:
                    newState.append(emptySpace)
        previousState = newState

    print("The beam is split " + str(splitCount) +" times")